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


######------------- SEED TABLES WITH FOREIGN KEY -------------######
def seed_fk():
  mycursor.execute("USE Monstermon") 
  ##Seed Trainers
  mycursor.executemany("""
    INSERT INTO Trainers (name, first_name, gender, ProfesseurID, is_professeur) 
    VALUES (%s, %s, %s, %s, %s)
    """, [
          ('Anderson', 'Ethan', 'Homme', None, 'Yes'),
          ('Martinez', 'Daniel', 'Homme', 1, 'No'),
          ('Johnson', 'Olivia', 'Femme', None, 'Yes'),
          ('Nguyen', 'Isabella', 'Femme', 11, 'No'),
          ('Smith', 'Michael', 'Homme', None, 'Yes'),
          ('García', 'Michel', 'Homme', 12, 'No'),
          ('Williams', 'James', 'Homme', None, 'No'),
          ('Rodriguez', 'Lucas', 'Homme', None, 'No'),
          ('Brown', 'Sophia', 'Femme', 5, 'No'),
          ('Patel', 'Harper', 'Femme', 3, 'No'),
          ('Clark', 'Mia', 'Femme', None, 'Yes'),
          ('Hall', 'Charlotte', 'Femme', None, 'Yes')
    ])
  mycursor.execute("""
    ALTER TABLE Trainers
    ADD CONSTRAINT fk_ProfesseurID
    FOREIGN KEY (ProfesseurID) REFERENCES Trainers(ID)
  """)
  
  ##Seed Monsters
  mycursor.executemany("""
    INSERT INTO Monsters (name, type, xp, hp, weight, size, PWRP, level, speciesID, captured, at, trainersID) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, [
          ('Grizzlor', 'Feu', 1000, 200, 20, 90, 150, 1, 10, 'Yes', '2022-12-14 11:10:00', 2),
          ('Azurika', 'Air', 2451, 100, 70, 70, 150, 1, 5, 'No', None, None),
          ('Crépulor', 'Feu', 8402, 200, 80, 80, 250, 2, 3, 'No', None, None),
          ('Vortexar', 'Air', 1203, 300, 90, 90, 350, 3, 6, 'Yes', '2023-07-14 19:36:58', 3),
          ('Gorgonix', 'Terre', 8321, 400, 100, 100, 400, 4, 10, 'Yes', '2023-06-28 11:20:08', 5),
          ('Zéphirium', 'Terre', 893, 500, 100, 100, 500, 5, 5, 'No', None, 4),
          ('Krypthona', 'Air', 193, 100, 30, 40, 200, 1, 3, 'No', None, 10),
          ('Glaciarax', 'Terre', 1893, 170, 60, 80, 300, 2, 6, 'Yes', '2022-10-19 21:07:11', 11),
          ('Infernion', 'Feu', 9903, 250, 100, 90, 400, 3, 6, 'Yes', '2023-01-18 07:23:09', 11),
          ('Sylvarath', 'Air', 10000, 500, 150, 100, 500, 4, 6, 'Yes', '2023-03-29 16:10:27', 12),
          ('Draconyx', 'Feu', 9213, 100, 10, 30, 70, 1, 2, 'No', None, 1),
          ('Abominix', 'Air', 9241, 180, 30, 40, 100, 2, 1, 'No', None, 3),
          ('Hydrokhan', 'Eau', 6000, 270, 40, 50, 200, 3, 2, 'No', None, None),
          ('Sombrodeus', 'Eau', 7313, 300, 45, 60, 300, 4, 5, 'Yes', '2023-09-11 09:42:00', 8),
          ('Nébulorok', 'Air', 513, 500, 50, 65, 500, 5, 7, 'Yes', '2023-06-28 14:20:08', 8),
          ('Terramorth', 'Terre', 64, 200, 25, 90, 150, 2, 8, 'No', None, 8),
          ('Zombalith', 'Feu', 22, 100, 70, 50, 200, 3, 1, 'No', None, 7),
          ('Phantasmagor','Feu',10,500,35,60,300,4,2,'Yes','2023-08-09 05:33:42',9),
          
          ('Luffy', 'Feu', 10, 500, 35, 60, 300, 4, 2, 'No', None, None),
          ('Toto', 'Feu', 10, 450, 35, 60, 300, 5, 7, 'Yes', '2023-08-09 05:33:42', 10),
          ('Salimatic', 'Feu', 10, 465, 35, 60, 300, 3, 5, 'No', None, None),
          ('Pharon', 'Feu', 10, 900, 35, 60, 300, 4, 6, 'No', None, None),
          ('Gazolina', 'Feu', 10, 670, 35, 60, 300, 2, 2, 'No', None, None),
          ('Salamesh', 'Feu', 10, 495, 35, 60, 300, 1, 4, 'Yes', '2023-08-09 05:33:42', 7),
          ('Psdd', 'Feu', 10, 401, 35, 60, 300, 5, 3, 'No', None, None),
          ('Toto', 'Feu', 10, 520, 35, 60, 300, 1, 1, 'Yes', '2023-08-09 05:33:42', 1),
          ('Fobar', 'Feu', 10, 450, 35, 60, 300, 2, 5, 'no', None, None),
          ('Foo', 'Feu', 10, 650, 35, 60, 300, 4, 3, 'Yes', '2023-08-09 05:33:42', 11),
          ('SIIIII', 'Feu', 10, 754, 35, 60, 300, 5, 8, 'no', None, None),
      ])
  
  ##Seed Sales
  mycursor.executemany("""
    INSERT INTO Sales (storeID, monstreID, trainersID, price, sale_at) 
    VALUES (%s, %s, %s, %s, %s)
    """, [
          (5, 12, 4, 30, '2026-06-05'),
          (7, 17, 12, 350, '2073-06-06'),
          (10, 9, 2, 65, '2019-5-15'),
          (1, 1, 5, 68, '2023-06-03'),
          (3, 3, 8, 541, '2005-06-18'),
          (4, 7, 1, 51, '2015-05-30')
    ])
  
  ##Seed ParticipationQuests
  mycursor.executemany("""
    INSERT INTO ParticipationQuests (monstreID, questID, participate_at)
    VALUES (%s, %s, %s)
    """,[
          (8, 3, '2026-06-04' ),
          (3, 5, '2078-12-23' ),
          (16, 7, '2066-05-30' ),
          (4, 4, '2009-07-15' ),
          (7, 6, '2002-11-03' ),
          (1, 2, '2005-12-07' ),
          (13, 5, '2005-11-08' ),
          (18, 6, '2005-06-01' ),
          (12, 8, '2005-01-22' ),
          (15, 1, '2015-04-17' ),
          (5, 2, '2001-05-21' )
      ])

  ##Seed Events  
  mycursor.executemany("""
    INSERT INTO Events (name, start_at, end_at, price, areneID)
    VALUES (%s, %s, %s, %s, %s)
    """,[
          ("Tournoi du Poing d'\Acier", '2023-04-15', '2023-04-18', 50, 3),
          ("L'Arène des Titans", '2023-06-10', '2023-06-12', 75, 3),
          ('La Basize  des Rois', '2023-08-20', '2023-08-20', 100, 4),
          ('Championnat Mondial des Monsters', '2023-09-15', '2023-09-18', 200, 3),
          ('La Guerre des Monsters', '2023-11-05', '2023-11-10', 60, 1),
          ('Le Duel des Titan', '2023-12-08', '2023-12-11', 45, 1),
          ("L'Ultimatum des Airs", '2023-12-01', '2024-01-05', 30, 3),
          ('Le Carnage des Monsteurs de Feu', '2024-01-25', '2024-02-14', 150, 4),
          ('La Grande Joute des Héros', '2024-02-12', '2024-02-20', 679, 1),
          ('Le Choc des Éléments', '2024-03-12', '2024-04-20', 1000, 3)
      ])  
  
  ##Seed ParticipationEvents
  mycursor.executemany("""
    INSERT INTO ParticipationEvents ( eventID, monstreID, participate_at)
    VALUES (%s, %s, %s)
    """,[
          (1,5, '2023-04-15'),
          (1,8, '2023-06-10'),
          (1,10, '2023-08-20'),
          (1,14, '2023-09-15'),
          (2,29, '2023-09-15'),
          (2,27, '2023-09-15'),
          (3,27, '2023-08-20'),
          (4,22, '2023-09-17'),
          (5,7, '2023-11-05'),
          (5,9, '2023-11-06'),
          (5,10, '2023-11-07'),
          (5,15, '2023-11-08'),
          (6,1, '2023-12-08'),
          (6,5, '2023-12-01'),
          (7,15, '2023-12-01'),
          (7,22, '2023-12-01'),
          (7,17, '2023-12-01'),
          (8,6, '2024-01-25'),
          (10,18, '2024-02-12'),
          (10,17, '2024-03-12'),
          (10,2, '2024-03-12')
      ])  

  ##Seed Equipment
  mycursor.executemany("""
    INSERT INTO Equipment (name, areneID, type)
    VALUES (%s, %s, %s)
    """,[
          ('Lac' ,1, 'Eau'),
          ('Fontaine',1, 'Eau'),
          ('Pierres',2, 'Terre'),
          ('Monuments',3, 'Terre')
      ])  

  ##Seed fights
  mycursor.executemany("""
    INSERT INTO fights (start_at, end_at, eventID)
    VALUES (%s, %s, %s)
    """,[
          ('2024-03-12','2024-04-01', 10),
          ('2024-03-20','2024-03-21', 10),
          ('2024-02-15','2024-02-16', 9),
          ('2023-11-07','2023-11-7', 5),
          ('2023-06-10','2023-06-12', 2),
          ('2023-12-01','2024-01-02', 7),
          ('2023-04-17','2023-04-18', 1),
          ('2023-11-06','2023-11-8', 5),
          ('2023-12-10','2023-12-11', 6),
          ('2023-08-20','2023-08-20', 3),
          ('2024-02-12','2024-02-12', 9),
          ('2024-01-25','2024-02-01', 8),
          ('2023-09-16','2023-09-17', 4),
          ('2024-01-30','2024-02-02', 8),
          ('2023-09-15','2023-09-16', 4),
          ('2023-08-20','2023-08-20', 3),
          ('2023-04-18','2023-04-18', 1),
          ('2024-01-28','2024-02-29', 8),
          ('2023-12-01','2023-12-12', 7),
      ])  

  ##Seed Species
  mycursor.executemany("""
    INSERT INTO fights_Monster ( fightID, monstreID, won)
    VALUES (%s, %s, %s)
    """,[
          (4, 5,'Yes'),
          (3, 8,'Yes'),
          (2, 15,'Yes'),
          (5, 22,'No'),
          (12, 9,'Yes'),
          (7, 12,'No'),
          (14, 26,'No'),
          (8, 25,'No'),
          (19, 13,'Yes'),
          (6, 29,'No'),
          (19, 23,'No'),
          (7, 10,'Yes'),
          (6, 20, 'No'),
          (2, 27,'No'),
          (5, 24,'Yes')
      ])
  
  mydb.commit()