#coding:utf8

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Source des données : https://www.data.gouv.fr/datasets/election-presidentielle-des-10-et-24-avril-2022-resultats-definitifs-du-1er-tour/

# Sources des données : production de M. Forriez, 2016-2023
with open("./data/resultats-elections-presidentielles-2022-1er-tour.csv","r") as fichier:
    contenu = pd.read_csv(fichier)
    
#Questions 5 à 7
Moyenne=[] 
Mediane=[]
Mode=[]
Ecarttype=[]
Ecartabsolu=[]
Etendue=[]
IQRs=[]
IDRs=[]
for colonne in contenu: 
    if contenu.dtypes [colonne] !=object:
        Moyenne.append(float(contenu[colonne].mean().round(2)))
        Mediane.append(int(contenu[colonne].median()))
        Mode.append(int(contenu[colonne].mode().iloc[0]))
        Ecarttype.append(float(contenu[colonne].std().round(2)))
        Ecartabsolu.append(float((contenu[colonne]-contenu[colonne].mean()).abs().mean().round(2)))
        Etendue.append(int(contenu[colonne].max()-contenu[colonne].min()))
        q1=contenu[colonne].quantile(0.25)
        q3  = contenu[colonne].quantile(0.75)
        d1  = contenu[colonne].quantile(0.10)
        d9  = contenu[colonne].quantile(0.90)
        IQRs.append(float(q3 - q1))
        IDRs.append(float((d9 - d1).round(2)))
        
print ("Moyenne:\t",Moyenne)
print ("Médiane:\t",Mediane)
print ("Mode:\t",Mode)
print ("Ecart type:\t",Ecarttype)
print ("Ecart absolu:\t",Ecartabsolu)
print ("Etendue:\t",Etendue)
print ("Distance interquartile:\t",IQRs)
print ("Distance interdécile:\t",IDRs)

#Question 8
for colonne in contenu :
    if contenu.dtypes [colonne] !=object:
        plt.figure()
        plt.boxplot(contenu[colonne])
        plt.title(colonne)
        plt.savefig("boite à moustache/"+colonne+".png")
        plt.close()
    
#Question 10
with open("./data/island-index.csv","r",encoding="latin-1") as fichier:
    doc = pd.read_csv(fichier,low_memory=False)
print (doc["Surface (kmÂ²)"])
limite=[0,10,25,50,100,2500,5000,10000]
categorie=[0,0,0,0,0,0,0,0]
for ile in doc["Surface (kmÂ²)"]:
    for i in range (len(limite)):
        if i==len(limite)-1 or ile <= limite [i+1]:
            categorie [i]+=1
print (categorie)
for i in range (len(categorie)-1):
    print ("Nombre d'îles entre",limite[i],"km² et",limite [i+1],"km²:",categorie[i])
print ("Nombre d'îles supérieur à 10 000 km²: ",categorie [7])


        
        