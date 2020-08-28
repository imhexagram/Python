import requests
from bs4 import BeautifulSoup
import csv
import json
from os import mkdir,getcwd

URL="https://intranet.iut-valence.fr/web/documents/"
headers={
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0;Win64,x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36",
    'Referer': "https://intranet.iut-valence.fr/web/connexion",
    'Host': "intranet.iut-valence.fr"
    }

url_site=input("URL de la page de prof : ")
prof=url_site.split("/")[-1]
path=input("La path de répertoir vous voulez télécharger(exemple: RT S2/M2103) : ").replace(" ","+")
path2=path
URL=URL+prof+"?path="+path

user=input("username : ")
passwd=input("password : ")
login={'_username':user,'_password':passwd}

s=requests.Session()
r1=s.get(url='https://intranet.iut-valence.fr/web/connexion',headers=headers,auth=(user,passwd))
r2=s.post(url='https://intranet.iut-valence.fr/web/verification',headers=headers,auth=(user,passwd),data=login)
r3=s.get(url=URL,headers=headers,auth=(user,passwd))
print(r3.status_code)

rep=input("chemin absolu de la répertoir de téléchargements (exemple D:/Users/iutuser/Desktop/TEST_Python) ou '1' pour chemin de cette script: ")
if rep=="1":
    rep=getcwd().replace("\\","/")+"/téléchargements_intranet"
    mkdir(rep)

def telecharger(rep,source):
    if '.' in source.split("/")[-1]:
        r4=s.get(url=source,headers=headers,auth=(user,passwd))
        name=source.split("/")[-1]
        with open(rep+'/'+name,'wb') as f:
            f.write(r4.content)
        print("téléchargement réussi : ",rep+'/'+name)
    elif '.' not in source.split("/")[-1]:
        name=source.split("/")[-1]
        rep=rep+'/'+name
        mkdir(rep)
        print("mkdir : ",rep)
        r4=s.get(url=source,headers=headers,auth=(user,passwd))
        p4=BeautifulSoup(r4.content,"html.parser")
        all_items=p4.find_all("td",attrs={'style':'text-align:left;'})
        global path
        path=path+"/"+name
        path3=path
        for i in all_items:
            path=path3
            source="https://intranet.iut-valence.fr"+i.find("a").get('href').replace(" ","+")
            if path in source:
                telecharger(rep,source)
    else:
        print("erreur")

p=BeautifulSoup(r3.content,"html.parser")
all_items=p.find_all("td",attrs={'style':'text-align:left;'})
for i in all_items:
    source="https://intranet.iut-valence.fr"+i.find("a").get('href')
    path=path2
    if path in source:
        telecharger(rep,source)
