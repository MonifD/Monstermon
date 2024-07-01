import sys
import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()
username = os.getenv("username")
password = os.getenv("password")

######------------- CONNECT TO DATABASE -------------######
mydb = mysql.connector.connect(
  host="localhost",
  user=username,
  password=password 
)
mycursor = mydb.cursor()

#### CREATE PROCEDURE MiseAJourMonster ####
def update_monster():
	mycursor.execute("USE Monstermon")
	mycursor.execute("""
	CREATE PROCEDURE IF NOT EXISTS MiseAJourMonster(
        IN monstreID INT,
        IN hp INT,
        IN level INT,
        IN PWRP INT,
        IN xp INT
    )
	BEGIN
		UPDATE Monsters
		SET
			hp = hp,
			level = level,
			PWRP = PWRP,
			xp = xp
		WHERE
			ID = monstreID;
		
		SELECT
			ID, name, type, hp, level, PWRP, xp, weight, size, speciesID, captured, at, trainersID
		FROM
			Monsters
		WHERE
			ID = monstreID;
	END
	""")
	print("Procedure MiseAJourMonster created successfully.")
    
#### CALL PROCEDURE MiseAJourMonster ####
def call_update_monster():
	update_monster()
	print("Entrez l'ID du monstre :")
	monstreID = int(input())
	print("Entrez les nouveaux points de vie :")
	hp = int(input())
	print("Entrez le nouveau niveau :")
	level = int(input())
	print("Entrez les nouveaux points de puissance :")
	PWRP = int(input())
	print("Entrez les nouveaux points d'expérience :")
	xp = int(input())
	mycursor.execute("USE Monstermon")
	mycursor.callproc('MiseAJourMonster', [monstreID, hp, level, PWRP, xp])
	for result in mycursor.stored_results():
		myresult = result.fetchall()
		print("+------+----------------+--------+----------+----------+--------+----------+--------+--------+------------+----------+----------------------+------------+")  
		print("| ID".ljust(6),"| name".ljust(16),"| type".ljust(8),"| hp".ljust(10),"| level".ljust(10),"| PWRP".ljust(8),"| xp".ljust(10),"| weight".ljust(8),"| size".ljust(8),"| speciesID".ljust(12),"| captured".ljust(10),"| at".ljust(22),"| trainersID".ljust(12),"|")
		print("+------+----------------+--------+----------+----------+--------+----------+--------+--------+------------+----------+----------------------+------------+")  
		for row in myresult:
			ID = str(row[0])
			name = str(row[1])
			type = str(row[2])
			hp = str(row[3])
			level = str(row[4])
			PWRP = str(row[5])
			xp = str(row[6])
			weight = str(row[7])
			size = str(row[8])
			speciesID = str(row[9])
			captured = str(row[10])
			at = str(row[11])
			trainersID = str(row[12])
			print(f"| {ID.ljust(4)} | {name.ljust(14)} | {type.ljust(6)} | {hp.ljust(8)} | {level.ljust(8)} | {PWRP.ljust(6)} | {xp.ljust(8)} | {weight.ljust(6)} | {size.ljust(6)} | {speciesID.ljust(10)} | {captured.ljust(8)} | {at.ljust(20)} | {trainersID.ljust(10)} |")
		print("+------+----------------+--------+----------+----------+--------+----------+--------+--------+------------+----------+----------------------+------------+")  
