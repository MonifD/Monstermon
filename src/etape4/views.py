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

#### VIEW QUEST STATISTIQUE ####
def req_view_quest():
	mycursor.execute("USE Monstermon")
	mycursor.execute("""
										
	CREATE VIEW IF NOT EXISTS StatistiqueMonsterQuete AS
	SELECT 
		Monsters.name AS Monster,
		IFNULL(ParticipationQuests.participate_at, '--------') AS Date_de_participation,
		IF(ParticipationQuests.questID IS NOT NULL, 'Yes', 'No') AS a_participe
	FROM 
		Monsters
	LEFT JOIN 
		ParticipationQuests ON Monsters.ID = ParticipationQuests.monstreID
	ORDER BY 
		ParticipationQuests.participate_at DESC
	""")
def view_quest():
	req_view_quest()
	mycursor.execute("USE Monstermon")
	mycursor.execute("""
										SELECT * FROM StatistiqueMonsterQuete
										""")
	myresult = mycursor.fetchall()
	print("+----------------+-----------------------+-------------+")  
	print("| Monster".ljust(16),"| Date_de_participation".ljust(23),"| a_participe".ljust(13),"|")
	print("+----------------+-----------------------+-------------+")  
	for row in myresult:
		Monster = str(row[0])
		Date_de_participation = str(row[1])
		a_participe = str(row[2])
		print(f"| {Monster.ljust(14)} | {Date_de_participation.ljust(21)} | {a_participe.ljust(11)} |")
	print("+----------------+-----------------------+-------------+") 
    
    
#### VIEW EVENTS STATISTIQUE ####
def req_view_events():
	mycursor.execute("USE Monstermon")
	mycursor.execute("""               
		CREATE VIEW IF NOT EXISTS StatistiqueEvenement AS
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
			COUNT(DISTINCT ParticipationEvents.monstreID) ASC
	""")
def view_events():
	req_view_events()
	mycursor.execute("USE Monstermon")
	mycursor.execute("""
										SELECT * FROM StatistiqueEvenement
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

