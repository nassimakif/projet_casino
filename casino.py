	#Les noms des vars à respecter (liste non exhaustive) :\n
	# name_user = le nom de l'utilisateur\n
	# nb_python = le nombre choisi par l'ordi aléatoirement !\n
	# nb_user = le nombre choisi par le user !\n
	# nb_coup = le nombre choisi par le user !\n 
	# level = niveau de jeu : 1, 2, 3 !\n     
	# mise = le montant de la mise du joueur !\n
	# dotation = la dotation initiale du joueur !\n
	# gain = le montant de la mise du joueur !\n
	# solde = le montant de la mise du joueur !\n  
	# mise moyenne est de "mise_moy"\n



# Les messages à imprimer (à respecter) : \n
# 	* Vous pouvez les personnaliser en soulignant les mots-d'intérêt et en adaptant un jeu de couleur suivant le type de message (perte / gain)

# 	* Proposer au joueur si il veut bien afficher les régles du jeu ?\n      
print("Voulez-vous afficher les regles du jeu ? (O/N)")


#
# 	\t- Le montant saisi n'est pas valide. Entrer SVP un montant entre 1 et 10 € :  ?\n    
# 	\t- Alors mon nombre est : ?\n
# 	\t- Je ne comprends pas ! Entrer SVP un nombre entre 1 et 10 :  ?\n
     

print("Je suis Python. Quel est votre pseudo ?")		#Je suis Python. Quel est votre pseudo ?
name_user = input()
print()
print("Le jeu commence, entrez votre mise ?")	 	#Le jeu commence, entrez votre mise ?
mise = input()
print()

# 	Hello René, vous avez 10 €, Très bien ! Installez vous SVP à la table de pari.\n\t\t\t Je vous expliquerai le principe du jeu : \n

print ("Hello,", name_user,"vous avez",mise, "$, Très bien ! Installez vous SVP à la table de pari")

# 	Je viens de penser à un nombre entre 1 et 10. Devinez lequel ?

# 2è façon sans True
from random import randrange
nb_ordi = randrange(0, 11, 1)
print("Mon choix = ", nb_ordi)
nb_user = -1
nb_coup = 0

while nb_ordi != nb_user :



	nb_user = int(input("Devine le nombre auquel je pense qui est compris entre 0 et 10\n"))
	if nb_user > nb_ordi :
		print ('Votre nbre est trop grand')
	elif nb_user < nb_ordi :
		print ('Votre nbre est trop petit')
	nb_coup += 1

	

print("Bingo ! Vous avez gagné en {} coup(s) !".format(nb_coup))


# 	Att : vous avez le droit à trois essais !\n
# 	Si vous devinez mon nombre dès le premier coup, vous gagnez le double de votre mise !\n
# 	Si vous le devinez au 2è coup, vous gagnez exactement votre mise !\n
# 	Si vous le devinez au 3è coup, vous gagnez la moitiè votre mise !\n    
# 	Si vous ne le devinez pas au 3è coup, vous perdez votre mise et vous avez le droit : 
#   de retenter votre chance avec l'argent qu'il vous reste pour reconquérir le level perdu.
# 	de quitter le jeu.\n
# 	\t- Dès que vous devinez mon nombre : vous avez le droit de quitter le jeu et de partir avec vos gains OU de continuer le jeu en passant au level supérieur.\n     
# 	\t- Vous avez dépassé le délai de 10 secondes" ! Vous perdez l'essai courant\n\t\t\t et il vous reste "E" essai(s) !\n
# 	\t- Votre nbre est trop grand !\n
# 	\t- Votre nbre est trop petit !\n
# 	\t- Il vous reste une chance !\n      
#  	\t- Bingo René, vous avez gagné en "N" coup(s) et vous avez emporté "E" € !\n
# 	\t- Vous avez perdu ! Mon nombre est "nb_python" !\n
# 	\t- Souhaitez-vous continuer la partie (O/N) ?\n
# 	\t- Je ne comprends pas votre réponse. Souhaitez-vous continuer la partie (O/N) ?\n
# 	\t- Au revoir ! Vous finissez la partie avec "M" €.\n    
# 	\t- Super ! Vous passez au Level 2.\n
# 	\t- Les statistiques du level 1 sont les suivantes : ...
# 	\t- Rappelez vous, le principe est le même sauf que mon nombre est maintenant entre 1 et 20 et\n\t\t vous avez le droit à 5 essais !\n
# 	\t- Entrez votre mise : ?\n
# 	\t- Erreur, votre mise est plus elevé que votre solde.\n
# 	\t- Entrer une mise inférieure ou égale à "S" € : ?\n
# 	\t ... \n  
# 	\t- Super ! Vous passez au Level 3 !\n
# 	\t- Les statistiques du level 2 sont les suivantes : ...    
# 	\t- Rappelez vous, le principe est le même sauf que mon nombre est entre 1 et 30 et\n\t\t vous avez le droit à 7 essais !\n 
# 	\t ... \n




# 	\t Bravo, vous avez gagné ! Les statistiques de la partie sont les suivantes : ... \n    
# 	\t- Rebonjour René, Content de vous revoir au Casino, prêt pour un nouveau challenge !\n.
# 	\t- Voici statistiques, depuis la 1è fois jj/mm/aaaa hh:mm :\n
# 	\t\t- Vos meilleures statistiques : 
# 	\t\t\t- Level le plus élevé atteint est "level",\n
# 	\t\t\t- Vous avez réussi à trouver le bon nombre dès le 1è coup "f" fois.\n
# 	\t\t\t- Le gain le plus elevé est
# 	\t\t\t- La mise la plus elevé est 
# 	\t\t\t- ...