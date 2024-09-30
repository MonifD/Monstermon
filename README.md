# SQL query

## 1er étape
création d'un schéma de base de donnée, qui contient toutes les informations du jeu, comme les dresseurs et les monstres etc...
## Mise en place de l'envirenement du travaille  
il faut dans un premier temps créer un envirenement virtuelle python 

Pour la création de l'envirenement virtuelle lancer la commande suivant 
```
 python3 -m venv <nom_de_votre_envirenement>
```

Pour se connecter à l'envirenement 
```
 source <nom_de_votre_envirenement>/bin/activate
 ```

puis lancer l'installation des paquets par la commande suivante

```
pip install -r requirements.txt
```

Si vous voulez ajouter des paquets vous pouvez le faire dans le fichier requirements.txt puis lancer la commande suivante pour prendre en compte les modification
```
pip install -r requirements.txt -U
```
## Lancement du script

Pour lancer le script 
```
python3 Monstermon.py help -> affiche tout les flages utilisables dans le code 

python3 Monstermon.py -<le_nom du flage>
```

Pour créer la base de donner 
```
python3 Monstermon.py -create
```

Pour alimenter la base de donner avec les données
```
python3 Monstermon.py -seed
```

pour supprimer la base de données
```
python3 Monstermon.py -delete
```
