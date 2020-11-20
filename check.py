from inputimeout import inputimeout, TimeoutOccurred

class Check:
    def __init__(self, nb_user, limiteMaxi, texte, txt):
        self.nb_user = nb_user
        self.limiteMaxi = limiteMaxi
        self.texte = texte
        self.txt = txt

    # Vérifie la saisie de l'utilisateur en fonction du temps qu'il dispose pour répondre et de son choix
    def checkSaisiNombre(nb_user, limiteMaxi):
        while int(nb_user) < 1 or int(nb_user) > int(limiteMaxi):
            try:
                nb_user = int(inputimeout(prompt='(10 secondes pour répondre) Je ne comprends pas ! Entrer SVP un nombre entre 1 et '+ str(limiteMaxi) + ':' , timeout=10))
            except TimeoutOccurred:
                print("Vous n'avez pas répondu assez vite")
        return nb_user

    # Verifie si le nombre est le bon
    def check_trouver_nombre(texte, nb_user):
        try:
            if nb_user != 0:
                print("\n" + str(texte))
            nb_user = inputimeout(prompt='\n(10 secondes pour répondre) \n Alors mon nombre est : ', timeout=10)
        except TimeoutOccurred:
            print("Vous n'avez pas répondu assez vite. Réssayer !")
        return int(nb_user)

    # verification saisie utilisateur (int)
    def checkInt(txt):
        bol = True
        while bol:
            try:
                valeur = int(input("\n" + txt))
                bol = False
            except ValueError:
                print("Ce n'est pas un entier!")
        return valeur
