class Rules:
    #affichage ou non des règles
    def rules():
        regles = 0
        while regles != 'o' or regles != 'O' or regles != 'n' or regles !='N':
            regles = input("\nVoulez-vous voir les règles ? (o ou n) : ")
            if regles == 'o' or regles == 'O':
                print("Si vous devinez mon nombre dès le premier coup, vous gagnez le double de votre mise !")
                print("Si vous le devinez au 2è coup, vous gagnez exactement votre mise !")
                print("Si vous le devinez au 3è coup, vous gagnez la moitiè votre mise !")
                print("Si vous ne le devinez pas au 3è coup, vous perdez votre mise et \nVous avez le droit :")
                print("\t- de retenter votre chance avec l'argent qu'il vous reste pour reconquérir le level perdu")
                print("\t- de quitter le jeu")
                print("Dès que vous devinez mon nombre : vous avez le droit de quitter le jeu et de partir avec vos gains OU de continuer le jeu en passant au level supérieur.")
                break
            elif regles == 'n' or regles =='N':
                print("Bonne chance à vous... ne pas lire les règles peut être préjudiciable....")
                break
            else:
                print("Je n'ai pas compris votre réponse, merci de répondre par oui ou non")

    