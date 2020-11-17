#Module
from random import *

#Fonction
def checkSaisiNombre(nb_user, max):
    while nb_user < 1 or nb_user > max:
        nb_user = int(input("Je ne comprends pas ! Entrer SVP un nombre entre 1 et 10 : "))
    return nb_user

#Saisie de début
name_user = str(input("Je suis Python. Quel est votre pseudo ? "))
print("Hello " + name_user + ", vous avez 10 €, Très bien ! Installez vous SVP à la table de pari.\n Je vous expliquerai le principe du jeu : ")
argent = 10
level = 0

while level < 4:
    if level == 0:
        print("1 - Level 1")
        print("4 - Sortir");
    elif level < 4:
        print("Super ! Vous passez au Level " + str(level+1));
        print(str(level+1) + " - Pour passer au level " + str(level+1))
        print("4 - Sortir");
    elif level == 4:
        print("4 - Sortir");
    
    level = int(input("Que voulez-vous faire : "))

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
        print("Je viens de penser à un nombre entre 1 et " + str(max) + ". Devinez lequel ? \n Att : vous avez le droit à trois essais !")
        print("\n Si vous devinez mon nombre dès le premier coup, vous gagnez le double de votre mise !")
        print("\n Si vous le devinez au 2è coup, vous gagnez exactement votre mise !")
        print("\n Si vous le devinez au 3è coup, vous gagnez la moitiè votre mise !")
        print("\n Si vous ne le devinez pas au 3è coup, vous perdez votre mise et \n vous avez le droit :")
        print("\n \t de retenter votre chance avec l'argent qu'il vous reste pour reconquérir le level perdu")
        print("\n \t de quitter le jeu")
        print("\n Dès que vous devinez mon nombre : vous avez le droit de quitter le jeu et de partir avec vos gains OU de continuer le jeu en passant au level supérieur.")

        #Montant de la mise
        if level == 1:
            mise = int(input("Le jeu commence, entrez votre mise : "))
        else:
            mise = int(input("Entrez votre mise : "))
            
        while mise < 1 or mise > argent:
            print("Le montant saisi n'est pas valide.")
            mise = int(input("Entrer SVP un montant entre 1 et " + argent + " € : "))

        #Nombre mystère
        nb_user = int(input("Alors mon nombre est : "))
        nb_user = checkSaisiNombre(nb_user, max)
        nb_coup = 1;
        while nb_user != nb_python or nb_user == "erreur":
            if nb_user < nb_python:
                nb_user = int(input("Votre nbre est trop petit ! \n Alors mon nombre est : "))
                nb_user = checkSaisiNombre(nb_user, max)
            if nb_user > nb_python:
                nb_user = int(input("Votre nbre est trop grand ! \n Alors mon nombre est : "))
                nb_user = checkSaisiNombre(nb_user, max)
            nb_coup += 1;
            if nb_coup == nb_essai-1 and nb_user != nb_python:
                print("Il vous reste une chance !")
            if nb_coup == nb_essai and nb_user != nb_python:
                nb_user = "erreur"
                break;

        #Résultat
        if nb_user == "erreur":
            print("Vous avez perdu ! Mon nombre est " + str(nb_python) + " !")
        else:
            #Calcul montant gagne
            if nb_coup == 1:
                argent = argent + (mise * 2)
            elif nb_coup == 2:
                argent = argent + mise
            elif nb_coup == 3:
                argent = argent + (mise/2)
            print("Bingo René, vous avez gagné en " + str(nb_coup) + " coup(s) et vous avez emporté " + str(argent) + "€ !")
    else:
        print("Au revoir ! Vous finissez la partie avec " + str(mise) + " €")