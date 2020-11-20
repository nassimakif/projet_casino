from check import Check

class Mise:
    def __init__(self, argent, level, nb_coup, mise, name_user):
        self.argent = argent
        self.level = level
        self.nb_coup = nb_coup
        self.mise = mise
        self.name_user = name_user

    # Retourn la mise
    def fonction_mise(argent, level):
        if level == 1:
            mise = Check.checkInt("\nLe jeu commence, entrez votre mise : ")
        else:
            mise = Check.checkInt("\nEntrez votre mise : ")
        while mise < 1 or mise > argent:
            print("Erreur, votre mise est plus elevé que votre solde.")
            mise = Check.checkInt("Entrer SVP un montant entre 1 et " + str(argent) + " € : ")
        return mise

    # affiche le montant gagner après la partie
    def argent_gagner(argent, nb_coup, mise, name_user):
        print("\nBingo " + name_user + ", vous avez gagné en " + str(nb_coup) + " coup(s) et vous avez misé " + str(mise) + "€ !")
        gain = 0
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
        return gain