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

######------------- CREATE DATABASE -------------######
def create_tables():
  creat_tables_queries = [
  "CREATE TABLE IF NOT EXISTS Trainers ( ID INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50) NOT NULL, first_name VARCHAR(50) NOT NULL, gender ENUM('Homme','Femme') NOT NULL, ProfesseurID INT,  is_professeur ENUM('Yes','No') NOT NULL DEFAULT 'No') ",
  "CREATE TABLE IF NOT EXISTS Species ( ID INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(100) NOT NULL) ",
  "CREATE TABLE IF NOT EXISTS Monsters ( ID INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50) NOT NULL, type ENUM('Feu','Eau','Plante','Électrique','Glace','Vol','Spectre','Acier','Poison','Air', 'Terre'), xp INT NOT NULL DEFAULT 0, hp INT NOT NULL DEFAULT 100, weight INT NOT NULL DEFAULT 0, size  INT NOT NULL DEFAULT 0, PWRP INT NOT NULL DEFAULT 0, level INT NOT NULL DEFAULT 1, speciesID INT, captured ENUM('Yes','No') NOT NULL DEFAULT 'No', at TIMESTAMP, trainersID INT, FOREIGN KEY (speciesID) REFERENCES Species (ID), FOREIGN KEY (trainersID) REFERENCES Trainers (ID) ) ",
  "CREATE TABLE IF NOT EXISTS Quests ( ID INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(100) NOT NULL, location VARCHAR(255), start_at DATE NOT NULL, end_at DATE, xp_wins INT NOT NULL DEFAULT 0) ",
  "CREATE TABLE IF NOT EXISTS ParticipationQuests ( ID INT PRIMARY KEY AUTO_INCREMENT, monstreID INT, questID INT, participate_at DATE, FOREIGN KEY (monstreID) REFERENCES Monsters (ID), FOREIGN KEY (questID) REFERENCES Quests (ID)) ",
  "CREATE TABLE IF NOT EXISTS Arenes ( ID INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(100) NOT NULL, location VARCHAR(255), Places INT NOT NULL DEFAULT 0, size_m2 INT NOT NULL DEFAULT 0 ) ",
  "CREATE TABLE IF NOT EXISTS Equipment ( ID INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(100) NOT NULL, areneID INT, type ENUM ('Casque', 'Armure', 'Bouclier', 'Eau', 'Terre'), FOREIGN KEY (areneID) REFERENCES Arenes (ID) ) ",
  "CREATE TABLE IF NOT EXISTS Events (  ID INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(100) NOT NULL, start_at DATE NOT NULL, end_at DATE NOT NULL, price INT NOT NULL DEFAULT 0, areneID INT, FOREIGN KEY (areneID) REFERENCES Arenes (ID) ) ",
  "CREATE TABLE IF NOT EXISTS ParticipationEvents ( eventID INT, monstreID INT, participate_at DATE NOT NULL, PRIMARY KEY (eventID, monstreID), FOREIGN KEY (eventID) REFERENCES Events (ID), FOREIGN KEY (monstreID) REFERENCES Monsters (ID) ) ",
  "CREATE TABLE IF NOT EXISTS Stores ( ID INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(100) NOT NULL, location VARCHAR(255) ) ",
  "CREATE TABLE IF NOT EXISTS Sales ( ID INT PRIMARY KEY AUTO_INCREMENT, storeID INT, monstreID INT, trainersID INT, price INT NOT NULL DEFAULT 0, sale_at DATE, FOREIGN KEY (storeID) REFERENCES Stores (ID), FOREIGN KEY (monstreID) REFERENCES Monsters (ID), FOREIGN KEY (trainersID) REFERENCES Trainers (ID) ) ",
  "CREATE TABLE IF NOT EXISTS fights (  ID INT PRIMARY KEY AUTO_INCREMENT, start_at DATE NOT NULL, end_at DATE NOT NULL, eventID INT, FOREIGN KEY (eventID) REFERENCES Events (ID) ) ",
  "CREATE TABLE IF NOT EXISTS fights_Monster ( fightID INT, monstreID INT, won ENUM('Yes','No') NOT NULL, PRIMARY KEY (fightID, monstreID), FOREIGN KEY (fightID) REFERENCES fights (ID), FOREIGN KEY (monstreID) REFERENCES Monsters (ID) ) "
  ]
  for query in creat_tables_queries:
      mycursor.execute(query)

def show_tables():
    mycursor.execute("SHOW TABLES")
    for x in mycursor:
        print(f"{x} created")
            
def create_database():
  mycursor.execute("CREATE DATABASE IF NOT EXISTS Monstermon")
  mycursor.execute("USE Monstermon")
  create_tables()
  show_tables()