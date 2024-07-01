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


######------------- Query BONUS-------------######
###---- LOCATION QUERY ----###
def location():
  print("""\n1/Requete :
        Obtenir la liste de toutes les adresses du jeu sans doublon.""")
  mycursor.execute("USE Monstermon")  
  mycursor.execute(""" 
    SELECT DISTINCT IFNULL(location, '-')
    FROM (
      SELECT 1, Quests.location
      FROM Quests
      UNION ALL
      SELECT 2, Arenes.location
      FROM Arenes
      UNION ALL
      SELECT 3, Stores.location
      FROM Stores
    ) AS location
    """)
  myresult = mycursor.fetchall()
  print("+------------------------------------------------------------+")  
  print("| Location".ljust(60),"|")
  print("+------------------------------------------------------------+")  
  for row in myresult:
    Location = str(row[0])
    print(f"| {Location.ljust(58)} |")
  print("+------------------------------------------------------------+")  
  