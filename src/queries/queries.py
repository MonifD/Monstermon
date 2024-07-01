import sys
import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()
username = os.getenv("username")
password= os.getenv("password")

######------------- CONECT TO DATABASE -------------######
mydb = mysql.connector.connect(
  host="localhost",
  user=username, 
  password=password
)
mycursor = mydb.cursor()


######------------- Query Monster -------------######
###---- QUERY 1/ ----###
def monster_catch():
  print("""\n1/Requete :
        Obtenir la liste des monsters capturés classé par la date de capture (Du plus récent au plus ancien):""")
  mycursor.execute("USE Monstermon")  
  mycursor.execute(""" 
    SELECT * 
      FROM Monsters
    WHERE captured = 'Yes'
    ORDER BY at DESC
    """)
  myresult = mycursor.fetchall()
  print("+----+--------------+-------+-------+-------+--------+-------+-------+-------+-----------+----------+---------------------+-------------+")  
  print("| ID".ljust(3),"| name".ljust(14),"| type".ljust(7),"| xp".ljust(7),"| hp".ljust(7),"| weight".ljust(6),"| size ".ljust(7),"| PWRP".ljust(7),"| level".ljust(7),"| speciesID".ljust(7),"| captured".ljust(8),"| at".ljust(21),"| trainersID  |")
  print("+----+--------------+-------+-------+-------+--------+-------+-------+-------+-----------+----------+---------------------+-------------+")  
  for row in myresult:
    ID = str(row[0])
    name = row[1]
    type = row[2]
    xp = str(row[3])
    hp = str(row[4])
    weight = str(row[5])
    size  = str(row[6])
    PWRP = str(row[7])
    level = str(row[8])
    speciesID = str(row[9])
    captured = row[10]
    at = str(row[11])
    trainersID = str(row[12])
    print(f"| {ID.ljust(2)} | {name.ljust(12)} | {type.ljust(5)} | {xp.ljust(5)} | {hp.ljust(5)} | {weight.ljust(6)} | {size .ljust(5)} | {PWRP.ljust(5)} | {level.ljust(5)} | {speciesID.ljust(9)} | {captured.ljust(8)} | {at.ljust(8)} | {trainersID.ljust(12)}|")
  print("+----+--------------+-------+-------+-------+--------+-------+-------+-------+-----------+----------+---------------------+-------------+")  

###---- QUERY 2/ ----###  
def monster_type():
  print("""\n2/Requete :
        Obtenir le nombre de monsters par type, vos deux champs devront être nommé respectivement “Type” et “Nombre”:""")
  mycursor.execute("USE Monstermon")  
  mycursor.execute(""" 
    SELECT 
      type AS Type, COUNT(*) AS Nombre
    FROM Monsters
    GROUP BY type
    """)
  myresult = mycursor.fetchall()
  print("+-------+---------+")  
  print("| Type".ljust(7),"| Nombers |")
  print("+-------+---------+")
  for row in myresult:
    Type = str(row[0])
    Nombers = str(row[1])
    print(f"| {Type.ljust(5)} |  {Nombers.ljust(7)}|")
  print("+-------+---------+")

###---- QUERY 3/ ----###  
def monster_trainers():
  print("""\n3/Requete :
        Obtenir pour chaque monster, son dresseur en affichant son nom et prénom dans le même champ nommé “dresseur” :  
        si le monster n’est associé à aucun dresseur, vous devez afficher “aucun” dans ce même champ:""")
  mycursor.execute("USE Monstermon")  
  mycursor.execute(""" 
    SELECT 
      Monsters.name AS monster_name,
    CONCAT(IFNULL(Trainers.name, 'Aucun'), ' ', IFNULL(Trainers.first_name, '')) AS dresseur
    FROM 
      Monsters
    LEFT JOIN Trainers ON Monsters.trainersID = Trainers.ID
    """)
  myresult = mycursor.fetchall()
  print("+-----------------+--------------------+")  
  print("| Monster".ljust(17),"| Dresseur".ljust(20),"|")
  print("+-----------------+--------------------+")
  for row in myresult:
    Monster = str(row[0])
    Dresseur = str(row[1])
    print(f"| {Monster.ljust(15)} |  {Dresseur.ljust(18)}|")
  print("+-----------------+--------------------+")
  
###---- QUERY 4/ ----###
def monster_sale():
  print("""\n4/Requete :
        Obtenir la liste des ventes : 
        chaque vente doit mentionner le magasin concerné, 
        le nom du monster vendu, le dresseur avec son nom et prénom, 
        le prix et la date de vente classée par la date de vente décroissant (Du plus récent au plus ancien)""")
  mycursor.execute("USE Monstermon")  
  mycursor.execute(""" 
    SELECT 
      Sales.sale_at AS Date_de_vente, 
      Stores.name AS Magasin, 
      Monsters.name AS Monster_vendu, 
    CONCAT(Trainers.name, ' ', Trainers.first_name) AS Nom_dresseur, Sales.price AS Prix
    FROM
      Sales
    JOIN 
      Stores ON Sales.storeID = Stores.ID
    JOIN 
      Monsters ON Sales.monstreID = Monsters.ID
    JOIN 
      Trainers ON Sales.trainersID = Trainers.ID
    ORDER BY Sales.sale_at DESC
    """)
  myresult = mycursor.fetchall()
  print("+--------------+-----------+------+---------------+-----------------+")  
  print("| Magasin".ljust(14),"| Monster".ljust(11),"| Prix".ljust(6),"| Date_de_vente".ljust(15),"| Nom_dresseur".ljust(17),"|")
  print("+--------------+-----------+------+---------------+-----------------+")  
  for row in myresult:
    Date_de_vente = str(row[0])
    Magasin = str(row[1])
    Monster_vendu = str(row[2])
    Nom_dresseur = str(row[3])
    Prix = str(row[4])
    print(f"| {Magasin.ljust(12)} | {Monster_vendu.ljust(9)} | {Prix.ljust(4)} | {Date_de_vente.ljust(13)} | {Nom_dresseur.ljust(15)} |")
  print("+--------------+-----------+------+---------------+-----------------+")  

###---- QUERY 5/ ----###
def stores_ca():
  print("""\n5/Requete :
        Obtenir le chiffre d'affaires total par magasin : 
        vous devez afficher les résultats avec un champ “Magasin” et un autre champ nommé “CA”.""")
  mycursor.execute("USE Monstermon")  
  mycursor.execute(""" 
    SELECT 
      Stores.name AS Magasin, SUM(Sales.price) AS CA
    FROM Sales
    JOIN Stores ON Sales.storeID = Stores.ID
    GROUP BY Stores.name
    """)
  myresult = mycursor.fetchall()
  print("+--------------+-----+")  
  print("| Magasin".ljust(14),"| CA".ljust(5),"|")
  print("+--------------+-----+")  
  for row in myresult:
    Magasin = str(row[0])
    CA = str(row[1])
    print(f"| {Magasin.ljust(12)} | {CA.ljust(3)} |")
  print("+--------------+-----+")  
  
###---- QUERY 6/ ----###
def quests_participe():
  print("""\n6/Requete :
        Obtenir les monsters ayant effectué ou non des quêtes. 
        Vous devez obtenir également la date à laquelle elle a été effectuée tout cela classé par de la plus récente à la plus plus ancienne.""")
  mycursor.execute("USE Monstermon")  
  mycursor.execute(""" 
    SELECT 
      Monsters.name AS Monster,
      ParticipationQuests.participate_at AS Date_de_participation,
      IF(ParticipationQuests.questID IS NOT NULL, 'Yes', 'No') AS a_participe
    FROM 
        Monsters
    LEFT JOIN 
        ParticipationQuests ON Monsters.ID = ParticipationQuests.monstreID
    ORDER BY 
        ParticipationQuests.participate_at DESC
    """)
  myresult = mycursor.fetchall()
  print("+--------------+-----------+------------+")  
  print("| Monstre".ljust(14),"| Participe".ljust(11),"| At".ljust(12),"|")
  print("+--------------+-----------+------------+")  
  for row in myresult:
    Monstre = str(row[0])
    At = str(row[1])
    Participe = str(row[2])
    print(f"| {Monstre.ljust(12)} | {Participe.ljust(9)} | {At.ljust(10)} |")
  print("+--------------+-----------+------------+")  

  
###---- QUERY 7/ ----###
def events():
  print("""\n7/Requete :
        Obtenir la liste de tous les événements même sans participant et combats : pour chaque évènement on souhaite avoir le nombre de monster qui y participe, l'arène 
        le nombre d'équipement disponible pour ces évènement et le nombre de combat effectués. 
        Tout cela devra être classé par le nombre de monster participant croissant (du plus petit au plus grand)""")
  mycursor.execute("USE Monstermon")  
  mycursor.execute(""" 
    SELECT 
    Events.name AS Event,
    Arenes.name AS Arene,
    COUNT(DISTINCT ParticipationEvents.monstreID) AS Nombre_de_monsters,
    COUNT(DISTINCT Equipment.ID) AS Nombre_d_equipement,
    COUNT(DISTINCT fights.ID) AS Nombre_de_combats
    FROM 
        Events
    LEFT JOIN 
        Arenes ON Events.areneID = Arenes.ID
    LEFT JOIN 
        ParticipationEvents ON Events.ID = ParticipationEvents.eventID
    LEFT JOIN 
        Equipment ON Equipment.areneID = Arenes.ID
    LEFT JOIN 
        fights ON Events.ID = fights.eventID
    GROUP BY 
        Events.ID, Events.name, Arenes.name
    ORDER BY 
        Nombre_de_monsters ASC
    """)
  myresult = mycursor.fetchall()
  print("+-----------------------------------+----------+--------------------+---------------------+-------------------+")  
  print("| Event".ljust(35),"| Arene".ljust(10),"| Nombre_de_monsters".ljust(20),"| Nombre_d_equipement".ljust(21),"| Nombre_de_combats".ljust(19),"|")
  print("+-----------------------------------+----------+--------------------+---------------------+-------------------+")  
  for row in myresult:
    Event = str(row[0])
    Arene = str(row[1])
    Nombre_de_monsters = str(row[2])
    Nombre_d_equipement = str(row[3])
    Nombre_de_combats = str(row[4])
    print(f"| {Event.ljust(33)} | {Arene.ljust(8)} | {Nombre_de_monsters.ljust(18)} | {Nombre_d_equipement.ljust(19)} | {Nombre_de_combats.ljust(17)} |")
  print("+-----------------------------------+----------+--------------------+---------------------+-------------------+")  


###---- QUERY 8/ ----###
def monster_feu():
  print("""\n8/Requete : 
        Obtenir la liste des monsters de type feu n’ayant pas été capturés, 
        disposant d’un niveau compris entre 2 et 5 et lui restant plus de 400 de point de vie. 
        Vous devez classer ce résultat du plus petit nombre de points de vie au plus grand.""")
  mycursor.execute("USE Monstermon")  
  mycursor.execute(""" 
    SELECT name AS Nom_du_monstre, hp AS Points_de_vie, level AS Niveau
    FROM Monsters
    WHERE type = 'Feu' 
      AND captured = 'No'
      AND level BETWEEN 2 AND 5
      AND hp > 400
    ORDER BY hp ASC
    """)
  myresult = mycursor.fetchall()
  print("+--------------+-------+-------+")  
  print("| Monster".ljust(14),"| Hp".ljust(7),"| Level".ljust(7),"|")
  print("+--------------+-------+-------+")  
  for row in myresult:
    Monster = str(row[0])
    Hp = str(row[1])
    Level = str(row[2])
    print(f"| {Monster.ljust(12)} | {Hp.ljust(5)} | {Level.ljust(5)} |")
  print("+--------------+-------+-------+")  
  
###---- QUERY 9/ ----###
def especes_monster():
  print("""\n9/Requete : 
        Obtenir la liste des espèces ayant au moins 4 monsters.""")
  mycursor.execute("USE Monstermon")  
  mycursor.execute(""" 
    SELECT Species.name AS Espece, COUNT(Monsters.ID) AS Nombre_de_monstres
    FROM Species
    JOIN Monsters ON Species.ID = Monsters.speciesID
    GROUP BY Species.name
    HAVING COUNT(Monsters.ID) >= 4
    """)
  myresult = mycursor.fetchall()
  print("+--------------------+--------------------+")  
  print("| Espece".ljust(20),"| Nombre_de_monstres".ljust(20),"|")
  print("+--------------------+--------------------+")  
  for row in myresult:
    Espece = str(row[0])
    Nombre_de_monstres = str(row[1])
    print(f"| {Espece.ljust(18)} | {Nombre_de_monstres.ljust(18)} |")
  print("+--------------------+--------------------+")  
