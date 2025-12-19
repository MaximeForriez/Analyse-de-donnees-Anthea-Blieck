#coding:utf8

import pandas as pd
import math
import scipy
import scipy.stats

#C'est la partie la plus importante dans l'analyse de données. D'une part, elle n'est pas simple à comprendre tant mathématiquement que pratiquement. D'autre, elle constitue une application des probabilités. L'idée consiste à comparer une distribution de probabilité (théorique) avec des observations concrètes. De fait, il faut bien connaître les distributions vues dans la séance précédente afin de bien pratiquer cette comparaison. Les probabilités permettent de définir une probabilité critique à partir de laquelle les résultats ne sont pas conformes à la théorie probabiliste.
#Il n'est pas facile de proposer des analyses de données uniquement dans un cadre univarié. Vous utiliserez la statistique inférentielle principalement dans le cadre d'analyses multivariées. La statistique univariée est une statistique descriptive. Bien que les tests y soient possibles, comprendre leur intérêt et leur puissance d'analyse dans un tel cadre peut être déroutant.
#Peu importe dans quelle théorie vous êtes, l'idée de la statistique inférentielle est de vérifier si ce que vous avez trouvé par une méthode de calcul est intelligent ou stupide. Est-ce que l'on peut valider le résultat obtenu ou est-ce que l'incertitude qu'il présente ne permet pas de conclure ? Peu importe également l'outil, à chaque mesure statistique, on vous proposera un test pour vous aider à prendre une décision sur vos résultats. Il faut juste être capable de le lire.

#Par convention, on place les fonctions locales au début du code après les bibliothèques.
def ouvrirUnFichier(nom):
    with open(nom, "r") as fichier:
        contenu = pd.read_csv(fichier)
    return contenu

#Théorie de l'échantillonnage (intervalles de fluctuation)
#L'échantillonnage se base sur la répétitivité.
print("Résultat sur le calcul d'un intervalle de fluctuation")

donnees = pd.DataFrame(ouvrirUnFichier("./data/Echantillonnage-100-Echantillons.csv"))
print (donnees)

mpour = int(donnees["Pour"].mean().round())
print("moyenne Pour :", mpour)

mcontre = int(donnees["Contre"].mean().round())
print("moyenne Contre :", mcontre)

so = int(donnees["Sans opinion"].mean().round())
print("moyenne Sans opinion :", so)

# --- Fréquences observées (à partir des 100 échantillons) ---
total_obs = mpour + mcontre + so
fp_obs = round(mpour / total_obs, 2)
fc_obs = round(mcontre / total_obs, 2)
fso_obs = round(so / total_obs, 2)

print("\nFréquences observées :")
print("Pour :", fp_obs)
print("Contre :", fc_obs)
print("Sans opinion :", fso_obs)

# --- Fréquences population mère ---
Fp = round(852 / 2185, 2)
Fc = round(911 / 2185, 2)
Fso = round(422 / 2185, 2)

print("\nFréquences réelles population mère :")
print("Pour :", Fp)
print("Contre :", Fc)
print("Sans opinion :", Fso)

# --- Fonction intervalle de fluctuation ---
z = 1.96  # seuil de 95%
N = 2185  # taille de la population mère

def intervalle_fluctuation(f, n):
    se = math.sqrt(f * (1 - f) / n)
    bas = round(f - z * se, 4)
    haut = round(f + z * se, 4)
    return bas, haut

# --- Intervalles pour chaque catégorie ---
IC_pour = intervalle_fluctuation(Fp, N)
IC_contre = intervalle_fluctuation(Fc, N)
IC_so = intervalle_fluctuation(Fso, N)

print("\nIntervalles de fluctuation 95% :")
print("Pour :", IC_pour)
print("Contre :", IC_contre)
print("Sans opinion :", IC_so)

# --- Comparaison ---
print("\nComparaison :")
print("Pour : Observé =", fp_obs, " | Attendu entre", IC_pour)
print("Contre : Observé =", fc_obs, " | Attendu entre", IC_contre)
print("Sans opinion : Observé =", fso_obs, " | Attendu entre", IC_so)


#Théorie de l'estimation (intervalles de confiance)
#L'estimation se base sur l'effectif.
print("Résultat sur le calcul d'un intervalle de confiance")

echantillon=donnees.iloc[0].to_list()
total=sum(echantillon)
frequence1=echantillon[0]/total
frequence2=echantillon[1]/total
frequence3=echantillon[2]/total
IC_f1=intervalle_fluctuation(frequence1,total)
IC_f2=intervalle_fluctuation(frequence2,total)
IC_f3=intervalle_fluctuation(frequence3,total)
print ("Total:",total)
print(frequence1,frequence2,frequence3)
print(IC_f1,IC_f2,IC_f3)

echantillon=donnees.iloc[1].to_list()
total=sum(echantillon)
frequence1=echantillon[0]/total
frequence2=echantillon[1]/total
frequence3=echantillon[2]/total
IC_f1=intervalle_fluctuation(frequence1,total)
IC_f2=intervalle_fluctuation(frequence2,total)
IC_f3=intervalle_fluctuation(frequence3,total)
print ("Total:",total)
print(frequence1,frequence2,frequence3)
print(IC_f1,IC_f2,IC_f3)

echantillon=donnees.iloc[2].to_list()
total=sum(echantillon)
frequence1=echantillon[0]/total
frequence2=echantillon[1]/total
frequence3=echantillon[2]/total
IC_f1=intervalle_fluctuation(frequence1,total)
IC_f2=intervalle_fluctuation(frequence2,total)
IC_f3=intervalle_fluctuation(frequence3,total)
print ("Total:",total)
print(frequence1,frequence2,frequence3)
print(IC_f1,IC_f2,IC_f3)


#Théorie de la décision (tests d'hypothèse)
#La décision se base sur la notion de risques alpha et bêta.
#Comme à la séance précédente, l'ensemble des tests se trouve au lien : https://docs.scipy.org/doc/scipy/reference/stats.html
print("Théorie de la décision")
loi1=ouvrirUnFichier("./data/Loi-normale-Test-1.csv").iloc[:,0]
loi2=ouvrirUnFichier("./data/Loi-normale-Test-2.csv").iloc[:,0]
loi1=pd.to_numeric(loi1,errors="coerce").dropna()   #tentative resoudre erreur
loi2=pd.to_numeric(loi2,errors="coerce").dropna()   #tentative resoudre erreur
stat1,res1=scipy.stats.shapiro(loi1)
stat2,res2=scipy.stats.shapiro(loi2)
print ("Loi 1:", round(stat1,4), round(res1,4))
print ("Loi 2:", round(stat2,4), round(res2,4))
