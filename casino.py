#Module
from random import *
from os import path
import os.path
from inputimeout import inputimeout, TimeoutOccurred
import json
from json.decoder import JSONDecodeError
from rules import Rules
from check import Check
from level import Level
from stats import Stats
from mise import Mise

#Saisie de début
Stats.creation_stats()
name_user = str(input("Je suis Python. Quel est votre pseudo ? "))
argent = Check.checkInt("Combien voulez-vous mettre dans le jeu : ")
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
            level = Level.permier_level(level)
        elif level < 3:
            level = Level.passage_level_superieur(level)
        elif level == 3:
            level = 4
            start = False
    else:
        level = Level.niveau_perdu(level)
        if level != 4 and argent == 0: 
            argent = Check.checkInt("\nVous avez tout perdu. Combien voulez-vous remettre ? : ")
    
    if level < 4:
        limiteMaxi = 0
        nb_essai = 0
        if level == 1:
            limiteMaxi = 10
            nb_essai = 3
        elif level == 2:
            limiteMaxi = 20
            nb_essai = 5
        elif level == 3:
            limiteMaxi = 30
            nb_essai = 7

        #Generation nombre
        nb_python = randint(1, limiteMaxi)
        print("Nombre mystere = " + str(nb_python))

        #Regle
        Rules.rules()
        print("\nJe viens de penser à un nombre entre 1 et " + str(limiteMaxi) + ". Devinez lequel ? \nAttention : vous avez le droit à " + str(nb_essai) + " essais !")
        
        #Montant de la mise
        mise = Mise.fonction_mise(argent, level)

        #Nombre mystere
        if nb_user == "erreur":
            nb_user = 0
        try:
            nb_user = inputimeout(prompt='(10 secondes pour répondre) \n\nAlors mon nombre est : ', timeout=10)
        except TimeoutOccurred:
            print("Vous n'avez pas répondu assez vite")
        if nb_user != 0:
            nb_user = Check.checkSaisiNombre(int(nb_user), limiteMaxi)
        nb_coup = 1
        while int(nb_user) != nb_python or int(nb_user) == "erreur":
            if int(nb_user) < nb_python:
                nb_user = Check.check_trouver_nombre("Votre nombre est trop petit !", int(nb_user), limiteMaxi)
            if int(nb_user) > nb_python:
                nb_user = Check.check_trouver_nombre("Votre nombre est trop grand !", int(nb_user), limiteMaxi)
            nb_coup += 1
            if nb_coup == nb_essai-1 and nb_user != nb_python:
                print("\nIl vous reste une chance !")
            if nb_coup == 0:
                nb_user = "erreur"
                break
            if nb_coup == nb_essai and nb_user != nb_python:
                nb_user = "erreur"
                break

        #Resultat
        if nb_user == "erreur":
            print("\nVous avez perdu ! Mon nombre est " + str(nb_python) + " !")
            argent = argent - mise
            print("Il vous reste " + str(argent) + "€")
        else:
            #Calcul montant gagne
            gain = Mise.argent_gagner(argent, nb_coup, mise, name_user)
            if level == 1:
                meilleure_gain = gain
                pire_gain = gain
            meilleure_gain = Stats.meilleureGain(gain, meilleure_gain)
            pire_gain = Stats.pireGain(gain, pire_gain)

        if level == 1:
            meilleure_mise = mise
            pire_mise = mise
        meilleure_mise = Stats.meilleureMise(mise, meilleure_mise)
        pire_mise = Stats.pireMise(mise, pire_mise)
    else:
        if level == 4:
            Stats.save_stats(meilleure_gain, pire_gain, meilleure_mise, pire_mise, name_user)

        print("\nAu revoir ! Vous finissez la partie avec " + str(argent) + " €")
        print("\nVotre meilleur gain est " + str(meilleure_gain)  + " €" )
        print("Votre meilleur mise est " + str(meilleure_mise)  + " €")
        print("Votre pire gain est " + str(pire_gain)  + " €")
        print("Votre pire mise est " + str(pire_mise) + " €")