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

######------------- DELETES ELEMENTS FROM TABLES -------------######
def delete_tables():
  mycursor.execute("USE Monstermon")
  
  mycursor.execute("DELETE FROM ParticipationQuests")
  mycursor.execute("DELETE FROM Quests")
  mycursor.execute("DELETE FROM fights_Monster")
  mycursor.execute("DELETE FROM fights")
  mycursor.execute("DELETE FROM ParticipationEvents")
  mycursor.execute("DELETE FROM Events")
  mycursor.execute("DELETE FROM Equipment")
  mycursor.execute("DELETE FROM Arenes")
  mycursor.execute("DELETE FROM Sales")
  mycursor.execute("DELETE FROM Stores")
  mycursor.execute("DELETE FROM Monsters")
  mycursor.execute("DELETE FROM Species")
  mycursor.execute("UPDATE Trainers SET ProfesseurID = NULL WHERE ProfesseurID IS NOT NULL;")
  mycursor.execute("DELETE FROM Monsters WHERE trainersID IN (SELECT trainersID FROM Trainers)")
  mycursor.execute("DELETE FROM Trainers")
  
  mydb.commit()