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

######------------- DROP TABLES AND DATABASE -------------######
def destroy_database():
  mycursor.execute("USE Monstermon")
  
  # DELETE TABLES
  mycursor.execute("DROP TABLE ParticipationQuests")
  mycursor.execute("DROP TABLE Quests")
  mycursor.execute("DROP TABLE fights_Monster")
  mycursor.execute("DROP TABLE fights")
  mycursor.execute("DROP TABLE ParticipationEvents")
  mycursor.execute("DROP TABLE Events")
  mycursor.execute("DROP TABLE Equipment")
  mycursor.execute("DROP TABLE Arenes")
  mycursor.execute("DROP TABLE Sales")
  mycursor.execute("DROP TABLE Stores")
  mycursor.execute("DROP TABLE Monsters")
  mycursor.execute("DROP TABLE Species")
  mycursor.execute("DROP TABLE Trainers")
  
  # THEN DELETE BATADASE
  mycursor.execute("DROP DATABASE Monstermon")

  mydb.commit()