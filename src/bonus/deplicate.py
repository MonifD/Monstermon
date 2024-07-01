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
###---- DUPLICATE QUERY ----###
def duplicate_equipment():
  print("""\n1/Requete :
        Insérez à nouveau les trois derniers équipements dans sa table respective (Tout doit être effectué dans une seule requête)""")
  mycursor.execute("USE Monstermon")  
  mycursor.execute(""" 
    INSERT INTO Equipment (name, areneID, type) 
    SELECT name, areneID, type
    FROM Equipment 
    ORDER BY ID DESC 
    LIMIT 3
    """)
  mydb.commit()
  mycursor.execute(""" 
    SELECT name, areneID, type
    FROM Equipment
    """)
  myresult = mycursor.fetchall()
  print("+------------+----------+--------+")  
  print("| name".ljust(12),"| areneID".ljust(10),"| type".ljust(8),"|")
  print("+------------+----------+--------+")  
  for row in myresult:
    name = str(row[0])
    areneID = str(row[1])
    type = str(row[2])
    print(f"| {name.ljust(10)} | {areneID.ljust(8)} | {type.ljust(6)} |")
  print("+------------+----------+--------+")  
  