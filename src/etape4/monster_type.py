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

#### CREATE PROCEDURE MonsterType IF NOT EXISTS ####
def create_procedure_monster_type():
	mycursor.execute("USE Monstermon")
	mycursor.execute("""
	CREATE PROCEDURE IF NOT EXISTS MonsterType(IN monster_type ENUM('Feu','Eau','Plante','Électrique','Glace','Vol','Spectre','Acier','Poison','Air','Terre'))
	BEGIN
		SELECT 
			ID, name, type, xp, hp, weight, size, PWRP, level, speciesID, captured, at, trainersID
		FROM 
			Monsters
		WHERE 
			type = monster_type;
	END
	""")
	print("Procedure MonsterType created successfully.")

#### CALL PROCEDURE MonsterType ####
def call_procedure_monster_type():
	create_procedure_monster_type()
	print("Quelle type de monstre voulez-vous ? (Feu, Eau, Plante, Électrique, Glace, Vol, Spectre, Acier, Poison, Air, Terre)")
	monster_type = input()
	mycursor.execute("USE Monstermon")
	mycursor.callproc('MonsterType', [monster_type])
	for result in mycursor.stored_results():
		myresult = result.fetchall()
		print("+------+----------------+--------+----------+----------+--------+--------+--------+--------+------------+----------+----------------------+------------+")  
		print("| ID".ljust(6),"| name".ljust(16),"| type".ljust(8),"| xp".ljust(10),"| hp".ljust(10),"| weight".ljust(8),"| size".ljust(8),"| PWRP".ljust(8),"| level".ljust(8),"| speciesID".ljust(12),"| captured".ljust(10),"| at".ljust(22),"| trainersID".ljust(12),"|")
		print("+------+----------------+--------+----------+----------+--------+--------+--------+--------+------------+----------+----------------------+------------+")  
		for row in myresult:
			ID = str(row[0])
			name = str(row[1])
			type = str(row[2])
			xp = str(row[3])
			hp = str(row[4])
			weight = str(row[5])
			size = str(row[6])
			PWRP = str(row[7])
			level = str(row[8])
			speciesID = str(row[9])
			captured = str(row[10])
			at = str(row[11])
			trainersID = str(row[12])
			print(f"| {ID.ljust(4)} | {name.ljust(14)} | {type.ljust(6)} | {xp.ljust(8)} | {hp.ljust(8)} | {weight.ljust(6)} | {size.ljust(6)} | {PWRP.ljust(6)} | {level.ljust(6)} | {speciesID.ljust(10)} | {captured.ljust(8)} | {at.ljust(20)} | {trainersID.ljust(10)} |")
		print("+------+----------------+--------+----------+----------+--------+--------+--------+--------+------------+----------+----------------------+------------+")  


