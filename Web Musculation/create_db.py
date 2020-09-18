import pymysql
from os import getcwd,listdir,chdir

reqCreation1="create table exercice ( id_e int(255) primary key auto_increment, nom_e varchar(64) not null, muscle varchar(64), repetition int(50));"
reqCreation2="create table participant ( id_p int(255) primary key auto_increment, nom_p varchar(64) not null, prenom varchar(64) not null);"
reqCreation3="create table liste ( id_l int(255) primary key auto_increment, nom_l varchar(64) not null);"
reqCreation4="create table contenir ( id_l integer references liste(id_l), id_e integer references exercice(id_e));"
reqCreation5="create table participer ( id_p integer references participant(id_p), id_l integer references liste(id_l));"
reqInsert11="insert into exercice values (1, 'traction', 'dos;bras(biceps)',5);"
reqInsert12="insert into exercice values (2, 'squat', 'jambes',5);"
reqInsert13="insert into exercice values (3, 'développé couché', 'pectoraux',5);"
reqInsert14="insert into exercice values (4, 'gainage', 'abdomen',1);"
reqInsert15="insert into exercice values (5, 'soulevé de terre', 'lombaires;cuisses',5);"
reqInsert21="insert into participant values (1, 'Ducci', 'Cris');"
reqInsert22="insert into participant values (2, 'Lee', 'Mary');"
reqInsert23="insert into participant values (3, 'Oxton', 'Lina');"
reqInsert24="insert into participant values (4, 'Hellscream', 'Garrosh');"
reqInsert25="insert into participant values (5, 'Raynor', 'James');"
reqInsert31="insert into liste values (1, 'Débutant');"
reqInsert32="insert into liste values (2, 'Test');"
reqInsert33="insert into liste values (3, 'Avancé');"
reqInsert34="insert into liste values (4, 'Perso_Garrosh');"
reqInsert35="insert into liste values (5, 'Perso_James');"
reqInsert41="insert into contenir values (1, 2);"
reqInsert42="insert into contenir values (1, 3);"
reqInsert43="insert into contenir values (2, 1);"
reqInsert44="insert into contenir values (2, 2);"
reqInsert45="insert into contenir values (3, 4);"
reqInsert46="insert into contenir values (4, 1);"
reqInsert47="insert into contenir values (5, 5);"
reqInsert51="insert into participer values (1, 1);"
reqInsert52="insert into participer values (2, 1);"
reqInsert53="insert into participer values (1, 2);"
reqInsert54="insert into participer values (2, 3);"
reqInsert55="insert into participer values (3, 2);"
reqInsert56="insert into participer values (4, 4);"
reqInsert57="insert into participer values (5, 5);"


host=input("votre host : ")
post=input("votre post (si vous tapez rien, ça va être la valeur automatique): ")
login=input("votre login : ")
passwd=input("votre password : ")
nom=input("nom de la base de donnée : ")
if post!="":
    db=pymysql.connect(host=host,post=post,user=login,passwd=passwd)
else:
    db=pymysql.connect(host=host,user=login,passwd=passwd)
c=db.cursor()
c.execute("create database {}".format(nom))
c.execute("use {}".format(nom))
c.execute(reqCreation1)
c.execute(reqCreation2)
c.execute(reqCreation3)
c.execute(reqCreation4)
c.execute(reqCreation5)
c.execute(reqInsert11)
c.execute(reqInsert12)
c.execute(reqInsert13)
c.execute(reqInsert14)
c.execute(reqInsert15)
c.execute(reqInsert21)
c.execute(reqInsert22)
c.execute(reqInsert23)
c.execute(reqInsert24)
c.execute(reqInsert25)
c.execute(reqInsert31)
c.execute(reqInsert32)
c.execute(reqInsert33)
c.execute(reqInsert34)
c.execute(reqInsert35)
c.execute(reqInsert41)
c.execute(reqInsert42)
c.execute(reqInsert43)
c.execute(reqInsert44)
c.execute(reqInsert45)
c.execute(reqInsert46)
c.execute(reqInsert47)
c.execute(reqInsert51)
c.execute(reqInsert52)
c.execute(reqInsert53)
c.execute(reqInsert54)
c.execute(reqInsert55)
c.execute(reqInsert56)
c.execute(reqInsert57)
db.commit()
print("Base créée : {}".format(db))
db.close()
