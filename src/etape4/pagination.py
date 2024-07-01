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

def pagination():
  print("how many result by pages ?")
  rows_in_page = [int(input())]
  print("which page do you want to see ?")
  page = [int(input())]

  LIMIT = rows_in_page[0]
  OFFSET = rows_in_page[0]*(page[0]-1)
  statement = [LIMIT, OFFSET]
  
  mycursor.execute("USE Monstermon")
  mycursor.execute("""
  SELECT ID, name, type, xp, hp, weight, size, PWRP,  level, speciesID, captured, IFNULL(at, '-----------------  '), IFNULL(trainersID, 'aucun') 
  FROM Monsters
  LIMIT %s 
  OFFSET %s""", statement)
  
  myresult = mycursor.fetchall()
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
    