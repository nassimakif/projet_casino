#Module
from random import *

#Fonction
def checkSaisiNombre(nb_user, max):
    while nb_user < 1 or nb_user > max:
        nb_user = int(input("Je ne comprends pas ! Entrer SVP un nombre entre 1 et 10 : "))
    return nb_user

#Saisie de début
name_user = str(input("Je suis Python. Quel est votre pseudo ? "))
argent = int(input("Combien voulez-vous mettre : "))
print("Hello " + name_user + ", vous avez " + str(argent) + " €, Très bien ! Installez vous SVP à la table de pari.\n\nJe vous expliquerai le principe du jeu ! ")
level = 0
nb_user = 0

while level < 4:
    if nb_user != "erreur":
        if level == 0:
            print("\t1 - Level 1")
            print("\t4 - Sortir")
            level = int(input("Que voulez-vous faire : "))
            while level != 1 and level != 4: 
                level = int(input("Réponse incorect, veuillez saisir le choix 1 ou 4 ! "))
        elif level < 3:
            level+=1
            print("\n\n Super ! Vous passez au Level " + str(level))
            print("\t" + str(level) + " - Pour passer au level " + str(level))
            print("\t4 - Sortir")
            levelaffichage = level
            level = int(input("Que voulez-vous faire : "))
            while levelaffichage != level and level != 4 : 
                level = int(input("Réponse incorect, veuillez saisir le choix " + str(levelaffichage) + " ou 4 ! "))
        elif level == 3:
            level = 4;
    else:
        print("\n\n Vous avez perdu au niveau " + str(level))
        print("\t" + str(level) + " - Pour recommencer au level " + str(level))
        print("\t4 - Sortir")
        level = int(input("Que voulez-vous faire : "))
        if level != 4: 
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

        #Génération nombre
        nb_python = randint(1, max)
        print("Nombre mystere = " + str(nb_python))

        #Régle
        print("\n\nJe viens de penser à un nombre entre 1 et " + str(max) + ". Devinez lequel ? \nAtt : vous avez le droit à trois essais !")
        print("Si vous devinez mon nombre dès le premier coup, vous gagnez le double de votre mise !")
        print("Si vous le devinez au 2è coup, vous gagnez exactement votre mise !")
        print("Si vous le devinez au 3è coup, vous gagnez la moitiè votre mise !")
        print("Si vous ne le devinez pas au 3è coup, vous perdez votre mise et \nVous avez le droit :")
        print("\t- de retenter votre chance avec l'argent qu'il vous reste pour reconquérir le level perdu")
        print("\t- de quitter le jeu")
        print("Dès que vous devinez mon nombre : vous avez le droit de quitter le jeu et de partir avec vos gains OU de continuer le jeu en passant au level supérieur.")

        #Montant de la mise
        if level == 1:
            mise = int(input("\n\nLe jeu commence, entrez votre mise : "))
        else:
            mise = int(input("\n\nEntrez votre mise : "))
            
        while mise < 1 or mise > argent:
            print("Erreur, votre mise est plus elevé que votre solde.")
            mise = int(input("Entrer SVP un montant entre 1 et " + str(argent) + " € : "))

        #Nombre mystère
        nb_user = int(input("\n\nAlors mon nombre est : "))
        nb_user = checkSaisiNombre(nb_user, max)
        nb_coup = 1
        while nb_user != nb_python or nb_user == "erreur":
            if nb_user < nb_python:
                nb_user = int(input("\nVotre nbre est trop petit ! \n Alors mon nombre est : "))
                nb_user = checkSaisiNombre(nb_user, max)
            if nb_user > nb_python:
                nb_user = int(input("\nVotre nbre est trop grand ! \n Alors mon nombre est : "))
                nb_user = checkSaisiNombre(nb_user, max)
            nb_coup += 1
            if nb_coup == nb_essai-1 and nb_user != nb_python:
                print("\nIl vous reste une chance !")
            if nb_coup == nb_essai and nb_user != nb_python:
                nb_user = "erreur"
                break

        #Résultat
        if nb_user == "erreur":
            print("Vous avez perdu ! Mon nombre est " + str(nb_python) + " !")
            print("Il vous reste " + str(argent-mise) + "€")
        else:
            #Calcul montant gagne
            print("Bingo " + name_user + ", vous avez gagné en " + str(nb_coup) + " coup(s) et vous avez misé " + str(mise) + "€ !")
            if nb_coup == 1:
                argent = argent + (mise * 2)
            elif nb_coup == 2:
                argent = argent + mise
            elif nb_coup == 3:
                argent = argent + (mise/2)
            print("Vous avez au total : " + str(argent) +"€")
            print("Vous avez gagné " + str(argent-mise) +"€")
           
    else:
        print("Au revoir ! Vous finissez la partie avec " + str(argent) + " €")