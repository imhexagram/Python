import cherrypy
import pymysql
import os,os.path
from mako.template import Template
from mako.lookup import TemplateLookup

mylookup=TemplateLookup(directories=['modeles'],module_directory='mako_modules')

#pour faire l'ordre du list
def takefirst(elem):
    return elem[0]

def takesecond(elem):
    return elem[1]


class musculation():

    def __init__(self):
        self.erreur=False
        print("Bonjour, avant le départ, je vous propose de créer la base de donnée par le fichier 'musculation.txt' dans ce répertoire")
        self.host=input("votre host : ")
        self.post=input("votre post (si vous tapez rien, ça va être la valeur par défaut): ")
        self.login=input("votre login MySQL : ")
        self.passwd=input("votre password MySQL : ")
        self.basededonne=input("nom de la base de donnée : ")
        try:
            if self.post!="":
                self.db=pymysql.connect(host=self.host,post=self.post,user=self.login,passwd=self.passwd,db=self.basededonne)
            else:
                self.db=pymysql.connect(host=self.host,user=self.login,passwd=self.passwd,db=self.basededonne)
        except TypeError:
            print("!!! TpyeError : vérifier type de données !!!")
            self.__init__()
        except pymysql.err.OperationalError:
            print("!!! pymysql.err.OperationalError : vérifier valeur de données !!!")
            self.__init__()
        self.c=self.db.cursor()

    @cherrypy.expose #page index
    def index(self):
        f=open('modeles/index.html',encoding="utf-8")
        s=f.read()
        return s

    @cherrypy.expose #page ajouter/supprimer
    def ASR(self, id_e, nom_e, muscule, repetition, id_l, nom_l, contenu, participe, id_p, nom_p, prenom_p, choix):
        self.erreur=False
        try:
            if choix=="ae":
                self.c.execute("insert into exercice values (NULL,'{}','{}',{})".format(nom_e, muscule, repetition))
            elif choix=="se":
                self.c.execute("delete from contenir where id_e={}".format(id_e))
                self.c.execute("delete from exercice where id_e={}".format(id_e))
            elif choix=="al":
                self.c.execute("insert into liste values (NULL,'{}')".format(nom_l))
                self.c.execute("select id_l from liste where nom_l='{}'".format(nom_l))
                id_l=int(self.c.fetchall()[0][0])
                for i in contenu.split(';'):
                    self.c.execute("insert into contenir values ({},{})".format(id_l,i))
                for i in participe.split(";"):
                    self.c.execute("insert into participer values ({},{})".format(i,id_l))
            elif choix=="sl":
                self.c.execute("delete from contenir where id_l={}".format(id_l))
                self.c.execute("delete from participer where id_l={}".format(id_l))
                self.c.execute("delete from liste where id_l={}".format(id_l))
            elif choix=="ap":
                self.c.execute("insert into participant values (NULL,'{}','{}')".format(nom_p, prenom_p))
            elif choix=="sp":
                self.c.execute("delete from participer where id_p={}".format(id_p))
                self.c.execute("delete from participant where id_p={}".format(id_p))
            else:
                raise Exception("bizzare, choix={}".format(choix))
        except:
            self.erreur=True
        self.db.commit()
        f=open('modeles/AS.html',encoding="utf-8")
        s=f.read()
        return s

    @cherrypy.expose #activité rechercher
    def ReR(self,textRe,ordre):
        self.erreur=False
        resulta1=[]
        resulta2=[]
        resulta3=[]
        #gestion ordre :
        desc=""
        if "desc" in ordre:
            ordre=str(ordre.split()[0])
            desc="desc"
        if textRe.replace(" ","").isalnum() or textRe=="":
            #table exercices :
            self.c.execute("select * from exercice where id_e like '%{0}%' or nom_e like '%{0}%' or muscle like '%{0}%' or repetition like '%{0}%' order by {1}".format(textRe,ordre+"_e "+desc))
            resulta1=self.c.fetchall()
            #table participant :
            self.c.execute("select * from participant where id_p like '%{0}%'  or nom_p like '%{0}%' or prenom like '%{0}%' order by {1}".format(textRe,ordre+"_p "+desc))
            resulta3=self.c.fetchall()
            #table liste : faire la transformation de data, les "id_e" chiffres dans table "liste" deviennent "nom_e" text par table "contenir"
            #les codes illisible sont pour changer "type". les variables nomé sans significatif sont sans significatif, ce sont des ponts pour changer.
            self.c.execute("select * from liste order by id_l")
            x=self.c.fetchall()
            b=""
            d=[]
            y=[]
            for id_l, nom_l in x:
                self.c.execute("select nom_e from exercice join contenir using(id_e) where id_l={}".format(id_l))
                a=self.c.fetchall()
                for i in range(len(a)):
                    b=b+"{}".format(a[i][0])+";"
                d.append(b)
                e=tuple(d)
                y.append(e)
                b=""
                d=[]
            self.c.execute("select count(id_p) from participer group by id_l order by id_l")
            z=self.c.fetchall()
            u=[]
            for i in range(len(x)):
                u.append(x[i]+y[i]+z[i])
            #table liste : supprimer les data non conforme
            resulta2=u.copy()
            for a,b,c,d in u:
                if textRe not in str(a) and textRe not in b and textRe not in c and textRe not in str(d):
                    resulta2.remove((a,b,c,d))
            #table liste: gestion ordre
            if ordre=="id":
                if desc=="desc":
                    resulta2.sort(key=takefirst,reverse=True)
                else :
                    resulta2.sort(key=takefirst)
            elif ordre=="nom":
                if desc=="desc":
                    resulta2.sort(key=takesecond,reverse=True)
                else:
                    resulta2.sort(key=takesecond)
            #surligner mot recherché :
            if textRe!="":
                resulta1=list(resulta1)
                for a in range(0,len(resulta1)):
                    resulta1[a]=list(resulta1[a])
                    for b in range(0,len(resulta1[a])):
                        if textRe in str(resulta1[a][b]):
                            resulta1[a][b]=str(resulta1[a][b]).split(textRe)
                            replace='<span style="background:yellow;">' + textRe + '</span>'
                            resulta1[a][b]=replace.join(resulta1[a][b])
                resulta2=list(resulta2)
                for a in range(0,len(resulta2)):
                    resulta2[a]=list(resulta2[a])
                    for b in range(0,len(resulta2[a])):
                        if textRe in str(resulta2[a][b]):
                            resulta2[a][b]=str(resulta2[a][b]).split(textRe)
                            replace='<span style="background:yellow;">' + textRe + '</span>'
                            resulta2[a][b]=replace.join(resulta2[a][b])
                resulta3=list(resulta3)
                for a in range(0,len(resulta3)):
                    resulta3[a]=list(resulta3[a])
                    for b in range(0,len(resulta3[a])):
                        if textRe in str(resulta3[a][b]):
                            resulta3[a][b]=str(resulta3[a][b]).split(textRe)
                            replace='<span style="background:yellow;">' + textRe + '</span>'
                            resulta3[a][b]=replace.join(resulta3[a][b])
        else:
            self.erreur=True
        mytemplate2=mylookup.get_template("Rechercher.html")
        return mytemplate2.render(variable1=resulta1, variable2=resulta2, variable3=resulta3,erreur=self.erreur)

    
if __name__=='__main__':
    rootPath=os.path.abspath(os.getcwd())
    print(rootPath)
    conf={
        '/':{'tools.sessions.on':True,
             'tools.staticdir.root':rootPath
            },
        '/static':{'tools.staticdir.on':True,
                   'tools.staticdir.dir':'modeles'
            },
        '/css':{'tools.staticdir.on':True,
                'tools.staticdir.dir':'modeles/css'
            },
        '/images':{'tools.staticdir.on':True,
                   'tools.staticdir.dir':'modeles/images'
            }
        }
    cherrypy.quickstart(musculation(),'/',conf)
