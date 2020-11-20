class Level:
    def __init__(self, level):
        self.level = level

    # retourne le level choisi par l'utilisateur à l'entree du programme
    def permier_level(level):
        print("\n----1 - Level 1")
        print("----4 - Sortir")
        level = int(input("Que voulez-vous faire : "))
        while level != 1 and level != 4: 
            level = int(input("Réponse incorect, veuillez saisir le choix 1 ou 4 ! "))
        return level

    # retourne le level (superieur) si le joueur gagne
    def passage_level_superieur(level):
        level+=1
        print("\nSuper ! Vous passez au Level " + str(level))
        print("\n----" + str(level) + " - Pour passer au level " + str(level))
        print("----4 - Sortir")
        levelprecedent = level
        level = int(input("Que voulez-vous faire : "))
        while levelprecedent != level and level != 4 : 
            level = int(input("Réponse incorect, veuillez saisir le choix " + str(levelprecedent) + " ou 4 ! "))
        return level

    # retourne le level si le joueur perd
    def niveau_perdu(level):
        print("\n\n Vous avez perdu au niveau " + str(level))
        if level != 1:
            level = level - 1
        print("----" + str(level) + " - Pour recommencer au level " + str(level))
        print("----4 - Sortir")
        level = int(input("Que voulez-vous faire : "))
        return level