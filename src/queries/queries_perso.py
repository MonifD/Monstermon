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


######------------- Query PERSONAL -------------######
###---- QUERY 1/ ----###
def xp_trainers():
  print("""\n1/Requete :
        Obtenir le total d'expérience (xp) accumulée par chaque dresseur.""")
  mycursor.execute("USE Monstermon")  
  mycursor.execute(""" 
    SELECT Trainers.name AS Nom_dresseur, Trainers.first_name AS Prenom_dresseur, SUM(Monsters.xp) AS Total_xp
    FROM Trainers
    JOIN Monsters ON Trainers.ID = Monsters.trainersID
    GROUP BY Trainers.ID, Trainers.name, Trainers.first_name
    """)
  myresult = mycursor.fetchall()
  print("+--------------+-----------------+----------+")  
  print("| Nom_dresseur".ljust(14),"| Prenom_dresseur".ljust(17),"| Total_xp".ljust(10),"|")
  print("+--------------+-----------------+----------+")  
  for row in myresult:
    Nom_dresseur = str(row[0])
    Prenom_dresseur = row[1]
    Total_xp = str(row[2])
    print(f"| {Nom_dresseur.ljust(12)} | {Prenom_dresseur.ljust(15)} | {Total_xp.ljust(8)} |")
  print("+--------------+-----------------+----------+")  
  
  
###---- QUERY 2/ ----###
def quest_monster():
  print("""\n2/Requete :
        obtenir le nombre total de quêtes effectuées par chaque monstre.""")
  mycursor.execute("USE Monstermon")  
  mycursor.execute(""" 
    SELECT Monsters.name AS Nom_du_monstre, COUNT(ParticipationQuests.ID) AS Nombre_de_quetes
    FROM Monsters
    LEFT JOIN ParticipationQuests ON Monsters.ID = ParticipationQuests.monstreID
    GROUP BY Monsters.ID, Monsters.name
    ORDER BY 
        Nombre_de_quetes DESC
    """)
  myresult = mycursor.fetchall()
  print("+----------------+------------------+")  
  print("| Nom_du_monstre".ljust(16),"| Nombre_de_quetes".ljust(18),"|")
  print("+----------------+------------------+")  
  for row in myresult:
    Nom_du_monstre = str(row[0])
    Nombre_de_quetes = str(row[1])
    print(f"| {Nom_du_monstre.ljust(14)} | {Nombre_de_quetes.ljust(16)} |")
  print("+----------------+------------------+")  
  
###---- QUERY 3/ ----###
def arene_info():
  print("""\n3/Requete :
        obtenir les détails des arènes avec le nombre d'équipements disponibles dans chaque arène.""")
  mycursor.execute("USE Monstermon")  
  mycursor.execute(""" 
    SELECT Arenes.name AS Nom_de_l_arene, COUNT(Equipment.ID) AS Nombre_d_equipements
    FROM Arenes
    LEFT JOIN Equipment ON Arenes.ID = Equipment.areneID
    GROUP BY Arenes.ID, Arenes.name
    """)
  myresult = mycursor.fetchall()
  print("+----------------+----------------------+")  
  print("| Nom_de_l_arene".ljust(16),"| Nombre_d_equipements".ljust(22),"|")
  print("+----------------+----------------------+")  
  for row in myresult:
    Nom_de_l_arene = str(row[0])
    Nombre_d_equipements = str(row[1])
    print(f"| {Nom_de_l_arene.ljust(14)} | {Nombre_d_equipements.ljust(20)} |")
  print("+----------------+----------------------+") 
  
     
###---- QUERY 4/ ----###
def quest_price():
  print("""\n4/Requete :
        Obtenir les événements avec le prix le plus élevé et le plus bas pour chaque arène.""")
  mycursor.execute("USE Monstermon")  
  mycursor.execute(""" 
    SELECT Arenes.name AS Nom_de_l_arene, MAX(Events.price) AS Prix_max, MIN(Events.price) AS Prix_min
    FROM Arenes
    JOIN Events ON Arenes.ID = Events.areneID
    GROUP BY Arenes.ID, Arenes.name
    """)
  myresult = mycursor.fetchall()
  print("+----------------+----------+----------+")  
  print("| Nom_de_l_arene".ljust(16),"| Prix_max".ljust(10),"| Prix_min".ljust(10),"|")
  print("+----------------+---------------------+")  
  for row in myresult:
    Nom_de_l_arene = str(row[0])
    Prix_max = str(row[1])
    Prix_min = str(row[2])
    print(f"| {Nom_de_l_arene.ljust(14)} | {Prix_max.ljust(8)} | {Prix_min.ljust(8)} |")
  print("+----------------+---------------------+")     
  
  
###---- QUERY 5/ ----###
def monster_weight():
  print("""\n5/Requete :
        obtenir les espèces de monstres avec un poids moyen supérieur à 50.""")
  mycursor.execute("USE Monstermon")  
  mycursor.execute(""" 
    SELECT Species.name AS Nom_de_l_espece, AVG(Monsters.weight) AS Poids_moyen
    FROM Species
    JOIN Monsters ON Species.ID = Monsters.speciesID
    GROUP BY Species.ID, Species.name
    HAVING AVG(Monsters.weight) > 50
    """)
  myresult = mycursor.fetchall()
  print("+-----------------+-------------+")  
  print("| Nom_de_l_espece".ljust(17),"| Poids_moyen".ljust(13),"|")
  print("+-----------------+-------------+")  
  for row in myresult:
    Nom_de_l_espece = str(row[0])
    Poids_moyen = str(row[1])
    print(f"| {Nom_de_l_espece.ljust(15)} | {Poids_moyen.ljust(11)} |")
  print("+-----------------+-------------+")  
