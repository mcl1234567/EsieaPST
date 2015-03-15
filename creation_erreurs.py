# Script en python de creation d erreur en Big data

import numpy as np
from random import randint
import string
import csv
import json

# CONSTANTES de creation CSV
#===============|========
_NB_LIGNES_ = 100000
_RATIO_TEL_ = 5
_RATIO_EMAIL_ = 5
_MODULO_TEL_ = _NB_LIGNES_ / (_NB_LIGNES_ * _RATIO_TEL_ / 100)
_MODULO_EMAIL_ = _NB_LIGNES_ / (_NB_LIGNES_ * _RATIO_EMAIL_ / 100)

# Recuperation de matrices de string ( String de 30 bytes )
# =============================================================
noms =              np.genfromtxt('/home/sb/esiea4A/PST/script/ressources/noms.txt',     dtype='|S30')
prenoms =           np.genfromtxt('/home/sb/esiea4A/PST/script/ressources/prenoms.txt',  dtype='|S30')
pays =              np.genfromtxt('/home/sb/esiea4A/PST/script/ressources/pays.txt',     dtype='|S30')
regionsTxt =        np.genfromtxt('/home/sb/esiea4A/PST/script/ressources/regions.txt',  dtype='|S30', delimiter=';')
codes_postauxTxt =  np.genfromtxt('/home/sb/esiea4A/PST/script/ressources/codes_postaux.txt', dtype='|S30', delimiter=';')
villesTxt =         np.genfromtxt('/home/sb/esiea4A/PST/script/ressources/villes.txt',   dtype='|S30', delimiter=';')

#json = open('PathToJson/data.json')
#jsonFile = json.load(json)

# lignes - colonnes
regions = regionsTxt[:, 0:1]
codes_postaux = codes_postauxTxt[:, 1:2]
villes = villesTxt[:, 1:2]

##############################################################

# Nombre de chiffres et validite des premiers chiffres
# Pays
# Region existante ou pas
# Validite du code
# Ville existante dans le pays ou pas

##############################################################

# Init tableaux : tab1 libelle
donneesLibelle = ["id", "nom", "prenom", "numero_tel", "pays", "region", "code_postal", "ville", "adresse_postale"]

# Insertion des donnees de Big data
# =========================================

# Init matrices - donnees
matA =  [[""] * len(donneesLibelle)]
matRes =  [[""] * len(donneesLibelle)] * _NB_LIGNES_

j = 0 # nom
k = 0 # prenom
l = 0 # tel
#m = 0 # pays
n = 0 # region
o = 0 # code postal
p = 0 # ville
#q = 0 # adresse postale

# Creation de telephones errones
# ==============================
def faireTelErr(nombreChiffre):
    baseTelFr1 = "+33"
    baseTelFr2 = "0"
    chiffresTel = [""] * nombreChiffre
    numeroTel = ""

    for j in range(nombreChiffre):
        chiffresTel[j] = str(randint(0, nombreChiffre))

        numeroTel = string.join(chiffresTel)        # Merger le tableau de chiffre
        numeroTel = numeroTel.replace(" ", "")      # Supprimer les espaces
        telsFrErr = baseTelFr1 + numeroTel

    return telsFrErr

# Creation de telephones formate en Fr
# ==============================
def faireTelFr():
    baseTelFr1 = "+33"
    baseTelFr2 = "0"
    nombreChiffreFr = 9
    chiffresTel = [""] * nombreChiffreFr
    numeroTel = ""

    for i in range(nombreChiffreFr):
        chiffresTel[i] = str(randint(0, nombreChiffreFr))

        numeroTel = string.join(chiffresTel)        # Merger le tableau de chiffre
        numeroTel = numeroTel.replace(" ", "")      # Supprimer les espaces
        telsFr = baseTelFr1 + numeroTel

    return telsFr

# Telephone France : +33 C CC CC CC CC ou 0C CC CC CC CC
# =========================================
# Creation de numeros de telephone finaux
def faireTelFinal():
    baseTelFr1 = "+33"
    baseTelFr2 = "0"
    leTel = ""

    # Creation de telephones errones
    if (i % _RATIO_TEL_) == 0:
        nombre = randint(5, 15)
        leTel = faireTelErr(nombre)
    # Creation de numeros de telephone formates en Fr
    else:
        leTel = faireTelFr()

    return leTel

# Creation d emails erronnes
def faireEmailErr():
    alea = randint(0, 3)

    compte = "toto"
    _arobase_ = "@"
    serveur = ["gmail", "hotmail", "yahoo" , "orange", "free"]
    extension = ["com", "fr"]

    email = compte + _arobase_
    email = email + serveur[randint(0, len(serveur)-1)]
    email = "."
    email = email + extension[randint(0, len(extension)-1)]

    # Creation des erreurs
    if alea == 0:
        # Compte a un seul caractere
        compte = ""
    elif alea == 1:
        # Arobase manquant
        _arobase_ = ""
    elif alea == 2:
        # Serveur / dommaine errone
        serveur = ["", "", "" , "", ""]
    elif alea == 3:
        # Serveur / dommaine errone
        extension = ["", ""]

    #email = compte + _arobase_ + serveur + "." + extension
    email = compte + _arobase_
    email = email + serveur[randint(0, len(serveur)-1)]
    email = email + "."
    email = email + extension[randint(0, len(extension)-1)]

    return email

# Creation d emails corrects
def faireEmailCorrect():
    compte = "toto"
    _arobase_ = "@"
    serveur = ["gmail", "hotmail", "yahoo" , "orange", "free"]
    extension = ["com", "fr"]

    email = compte + _arobase_
    email = email + serveur[randint(0, len(serveur)-1)]
    email = email + "."
    email = email + extension[randint(0, len(extension)-1)]

    return email

# Creation d emails finaux
def faireEmailFinal():
    lEmail = ""

    # Creation d emails errones
    if (i % _RATIO_EMAIL_) == 0:
        lEmail = faireEmailErr()
    # Creation d emails corrects
    else:
        lEmail = faireEmailCorrect()

    return lEmail

# Creation des lignes CSV
# ===============================================
for i in range(_NB_LIGNES_):

    # Telephone France : +33 C CC CC CC CC ou 0C CC CC CC CC
    leTel = faireTelFinal()
    lEmail = faireEmailFinal()

    # Indice au hasard pour la selection
    # =========================================
    idNomH =    randint(0, len(noms)-1)
    idPrenomH = randint(0, len(prenoms)-1)
    idRegionH = randint(0, len(regions)-1)
    idCodeH =   randint(0, len(codes_postaux)-1)
    idVilleH =  randint(0, len(villes)-1)

    # Transformation de tableaux en strings
    # =========================================
    leNom =         noms[idNomH]
    lePrenom =      prenoms[idPrenomH]
    lePays =        "France"
    laRegion =      string.join(regions[idRegionH])
    leCodePostal =  string.join(codes_postaux[idCodeH])
    laVille =       string.join(villes[idVilleH])
    lAdresse =      "tutu"

    # Creation de la ligne CSV
    # =========================================
    matA = [i, leNom, lePrenom, leTel, lEmail, lePays, laRegion, leCodePostal, laVille, lAdresse]

    # Incrementations des indices
    # =========================================
    j = j + 1
    k = k + 1
    l = l + 1
    #m = m + 1
    n = n + 1
    o = o + 1
    p = p + 1
    #q = q + 1

    # Matrice Csv - donnees
    matRes[i] = matA
# fin du for

"""
# test
print donneesLibelle

for i in range(_NB_LIGNES_):
    print matRes[i]
"""

# Ecriture du CSV
# =========================================
c = csv.writer(open("fichier_export.csv", "wb"))
c.writerow(donneesLibelle)
for i in range(_NB_LIGNES_):
    c.writerow(matRes[i])
