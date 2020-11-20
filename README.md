## Titre du projet

Le projet s'appelle "Python Casino". Il s'agit d'un programme codé en python et qui permet de simuler une réplique d'un jeu type casino directement via le terminal.

## Pre-réquis d'installation

**Liste des imports natif à python :**
```python
from os import path 
import os.path
from inputimeout import inputimeout, TimeoutOccurred
import json
from json.decoder import JSONDecodeError
```

**Liste des imports de packages crées pour le projet:**

from rules import Rules 
from check import Check 
from level import Level 
from stats import Stats 
from mise import Mise


## Démarrage du programme

Pour lancer le programme casino.py, accédez au répertoire où se trouve le fichier casino.py. Ensuite tapez la commande: python casino.py

## Règles du programme

Le jeu comporte quatre levels. Lors de chaque level, Python tire un nombre : level 1 (entre 1 et 10),level2 (1 et 20), level3 (1 et 30). C'est à vous de deviner le nombre mystérieux avec 3 essais (en tout)lors du 1è level, 5 lors du 2è level et 7 essais lors du 3è level. Chaque essai ne durera pas plus
de 10 secondes. En dépassant ce délai, vous perdez votre essai.
Lorsque vous gagnez un level et/ou terminer une partie, Python fournit des statistiques (voir ci-dessous).
Quand vous souhaitez quitter le jeu, Python mets en place un compteur jusqu'à 10 secondes pour valider votre décision.
Au-delà, Python quitte le jeu.

## Capture d'écran

![Capture](/image/image.png)

Un utilisateur joue avec Python.

## Fichiers contenus dans le projet

Projet Casino.ipynb
README.md
casino.py
check.py
level.py
mise.py
rules.py
stats.json
stats.py

## Livraison et déployement

Un premier livrable fonctionnel est disponible le 20/11/2020. 

## Axes d'amélioration

Des axes d'améliorations avec une librairie tel que Pandas pour un affichage de graphique en lien avec notre programme serait une amélioration possible. Egalement l'utilisation de Numpy pour l'aspect statistiques et enfin la possibilité d'intégrer le programme sur du Web avec Flask. De plus, MongoDB pourrait être utilisé avec le fichier JSON. Pour éviter tous problèmes avec l'outil Git, il faudrait que nous utilisions différentes branches. 


## Méthodologie et gestion de projet

Pour ce projet, nous avons utilisé la méthodologie Kanban.


## Auteurs

Ce projet a ete realisé par des eleves des promo AW et CS 22.2 , dont voici la liste :

**Jean TALGORN-THOMAS AW
<br/>Benjamin PRADON AW
<br/>Eliot DEMANGEL CS
<br/>Nassim AKIF AW
<br/>Laetitia HAMDIS CS
<br/>Marc NTUMBA CS
<br/>Mamadou CISSOKHO CS**
