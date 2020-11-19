#Module
from random import *
from os import path
import os.path
from inputimeout import inputimeout, TimeoutOccurred
import json
from json.decoder import JSONDecodeError
from datetime import datetime

#Fonctions
def checkSaisiNombre(nb_user, max):
    while int(nb_user) < 1 or int(nb_user) > int(max):
        try:
            nb_user = int(inputimeout(prompt='(10 secondes pour répondre) Je ne comprends pas ! Entrer SVP un nombre entre 1 et '+ str(max) + ':' , timeout=10))
        except TimeoutOccurred:
            print("Vous n'avez pas répondu assez vite")
    return nb_user

def rules():
    regles = input("Voulez-vous voir les règles ? (o ou n) : ")
    if regles == 'o' or regles == 'O':
        print("Si vous devinez mon nombre dès le premier coup, vous gagnez le double de votre mise !")
        print("Si vous le devinez au 2è coup, vous gagnez exactement votre mise !")
        print("Si vous le devinez au 3è coup, vous gagnez la moitiè votre mise !")
        print("Si vous ne le devinez pas au 3è coup, vous perdez votre mise et \nVous avez le droit :")
        print("\t- de retenter votre chance avec l'argent qu'il vous reste pour reconquérir le level perdu")
        print("\t- de quitter le jeu")
        print("Dès que vous devinez mon nombre : vous avez le droit de quitter le jeu et de partir avec vos gains OU de continuer le jeu en passant au level supérieur.")
    elif regles == 'n' or regles =='N':
        print("Bonne chance à vous... ne pas lire les règles peut être préjudiciable....")
    else:
        print("Je n'ai pas compris votre input")

def fonction_mise(argent):
    if level == 1:
        mise = int(input("\n\nLe jeu commence, entrez votre mise : "))
    else:
        mise = int(input("\n\nEntrez votre mise : "))
    while mise < 1 or mise > argent:
        print("Erreur, votre mise est plus elevé que votre solde.")
        mise = int(input("Entrer SVP un montant entre 1 et " + str(argent) + " € : "))
    return mise

def check_trouver_nombre(texte, nb_user, max):
    try:
        if nb_user != 0:
            print("\n" + str(texte))
        nb_user = inputimeout(prompt=' \n (10 secondes pour répondre) \n Alors mon nombre est : ', timeout=10)
    except TimeoutOccurred:
        print("Vous n'avez pas répondu assez vite")
    if nb_user != 0:
        nb_user = checkSaisiNombre(int(nb_user), max)
    return int(nb_user)

def permier_level(level):
    print("\t1 - Level 1")
    print("\t4 - Sortir")
    level = int(input("Que voulez-vous faire : "))
    while level != 1 and level != 4: 
        level = int(input("Réponse incorect, veuillez saisir le choix 1 ou 4 ! "))
    return level

def passage_level_superieur(level):
    level+=1
    print("\n\n Super ! Vous passez au Level " + str(level))
    print("\t" + str(level) + " - Pour passer au level " + str(level))
    print("\t4 - Sortir")
    levelprecedent = level
    level = int(input("Que voulez-vous faire : "))
    while levelprecedent != level and level != 4 : 
        level = int(input("Réponse incorect, veuillez saisir le choix " + str(levelprecedent) + " ou 4 ! "))
    return level

def niveau_perdu(level):
    print("\n\n Vous avez perdu au niveau " + str(level))
    if level != 1:
        level = level - 1
    print("\t" + str(level) + " - Pour recommencer au level " + str(level))
    print("\t4 - Sortir")
    level = int(input("Que voulez-vous faire : "))
    return level

def meilleureGain(gain, meilleure_gain):
    if gain > meilleure_gain:
        return gain
    else:
        return meilleure_gain

def meilleureMise(mise, meilleure_mise):
    if mise > meilleure_mise:
        return mise
    else:
        return meilleure_mise

def pireMise(mise, pire_mise):
    if pire_mise < mise:
        return pire_mise
    else:
        return mise

def pireGain(gain, pire_gain):
    if pire_gain < gain:
        return pire_gain
    else:
        return gain

stat = {
            "list_pseudo" : []
        }
if not path.exists("stats.json"):
    with open("stats.json", "w") as file:
        json.dump(stat, file)
        file.close()

#Saisie de début
name_user = str(input("Je suis Python. Quel est votre pseudo ? "))
argent = int(input("Combien voulez-vous mettre : "))
print("Hello " + name_user + ", vous avez " + str(argent) + " €, Très bien ! Installez vous SVP à la table de pari.\n\nJe vous expliquerai le principe du jeu ! ")
level = 0
nb_user = 0
start = True
meilleure_gain = 0
pire_gain = 0
meilleure_mise = 0
pire_mise = 0

while level < 4:
    if nb_user != "erreur":
        if level == 0:
            level = permier_level(level)
        elif level < 3:
            level = passage_level_superieur(level)
        elif level == 3:
            level = 4
            start = False
    else:
        level = niveau_perdu(level)
        if level != 4 and argent == 0: 
            argent = int(input("Vous avez tout perdu. Combien voulez-vous remettre ? : "))

    if level < 4:
        if level == 1:
            max = 10
            nb_essai = 3
        elif level == 2:
            max = 20
            nb_essai = 5
        elif level == 3:
            max = 30
            nb_essai = 7

        #Generation nombre
        nb_python = randint(1, max)
        print("Nombre mystere = " + str(nb_python))

        #Regle
        rules()
        print("\n\nJe viens de penser à un nombre entre 1 et " + str(max) + ". Devinez lequel ? \nAtt : vous avez le droit à " + str(nb_essai) + " essais !")
        
        #Montant de la mise
        mise = fonction_mise(argent)

        #Nombre mystere
        try:
            nb_user = inputimeout(prompt='(10 secondes pour répondre) \n\nAlors mon nombre est : ', timeout=10)
        except TimeoutOccurred:
            print("Vous n'avez pas répondu assez vite")
        if nb_user != 0:
            nb_user = checkSaisiNombre(int(nb_user), max)
        nb_coup = 1
        while int(nb_user) != nb_python or int(nb_user) == "erreur":
            if int(nb_user) < nb_python:
                nb_user = check_trouver_nombre("Votre nombre est trop petit !", int(nb_user), max)
            if int(nb_user) > nb_python:
                nb_user = check_trouver_nombre("Votre nombre est trop grand !", int(nb_user), max)
            nb_coup += 1
            if nb_coup == nb_essai-1 and nb_user != nb_python:
                print("\nIl vous reste une chance !")
            if nb_user == 0:
                nb_user = "erreur"
                break
            if nb_coup == nb_essai and nb_user != nb_python:
                nb_user = "erreur"
                break

        #Resultat
        if nb_user == "erreur":
            print("Vous avez perdu ! Mon nombre est " + str(nb_python) + " !")
            argent = argent - mise
            print("Il vous reste " + str(argent) + "€")
        else:
            #Calcul montant gagne
            print("Bingo " + name_user + ", vous avez gagné en " + str(nb_coup) + " coup(s) et vous avez misé " + str(mise) + "€ !")
            if nb_coup == 1:
                gain = mise * 2
                argent = argent + gain
            elif nb_coup == 2:
                gain = mise
                argent = argent + gain
            elif nb_coup == 3:
                gain = mise/2
                argent = argent + gain
            print("Vous avez au total : " + str(argent) +"€")
            print("Vous avez gagné " + str(argent-mise) +"€")
            if level == 1:
                meilleure_gain = gain
                pire_gain = gain
            meilleure_gain = meilleureGain(gain, meilleure_gain)
            pire_gain = pireGain(gain, pire_gain)

        if level == 1:
            meilleure_mise = mise
            pire_mise = mise
        meilleure_mise = meilleureMise(mise, meilleure_mise)
        pire_mise = pireMise(mise, pire_mise)
    else:
        donnees = { name_user : {
             'meilleure gain':[meilleure_gain],
             'pire gain': [pire_gain],
             'meilleure mise': [meilleure_mise],
             'pire mise': [pire_mise]
             }
            }
        print('level = ' + str(level))
        if level == 4:
            with open("stats.json", "r") as file:
                data_json = json.load(file)
                file.close()
                with open("stats.json", "w") as file:
                    if name_user in data_json["list_pseudo"]:  
                        data_json[name_user]['meilleure gain'].append(meilleure_gain)
                        data_json[name_user]['pire gain'].append(pire_gain)
                        data_json[name_user]['meilleure mise'].append(meilleure_mise)
                        data_json[name_user]['pire mise'].append(pire_mise)
                        json.dump(data_json, file)
                    else:
                        data_json["list_pseudo"].append(name_user)
                        data_json.update(donnees)
                        json.dump(data_json, file)


            print("Au revoir ! Vous finissez la partie avec " + str(argent) + " €")
            print("Votre meilleur gain est " + str(meilleure_gain)  + " €" )
            print("Votre meilleur mise est " + str(meilleure_mise)  + " €")
            print("Votre pire gain est " + str(pire_gain)  + " €")
            print("Votre pire mise est " + str(pire_mise) + " €")