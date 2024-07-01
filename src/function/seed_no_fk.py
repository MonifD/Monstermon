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

######------------- SEED TABLES WITHOUT FOREIGN KEY -------------######
def seed_no_fk():
  mycursor.execute("USE Monstermon") 
  #Seed Species
  mycursor.executemany("""
    INSERT INTO Species (name) 
    VALUES (%s)
    """, [
          ('Fluffernox',), ('Glacéphalosaurus',), ('Pluminsecte',), ('Bulbosarbre',),('Aquastruth',),
          ('Pyrovolcanix',), ('Ventisphère',), ('Cristalpuma',), ('Sylvabulle',), ('Gravifouetteur',)
    ])
  
  ##Seed Quests
  mycursor.executemany("""
    INSERT INTO Quests (name, location, start_at, end_at, xp_wins)
    VALUES (%s, %s, %s, %s, %s)
    """, [ 
          ('La Quête du Trésor Perdu', '123 Rue des Mystères Ombreville', '2023-04-10', '2023-04-20', 350), 
          ('La Chasse aux Créatures Mythiques','Forêt Enchantée Clairière des Lutins','2023-06-05',None,2000), 
          ("L\'Expédition dans les Profondeurs", "Cité Sous-Marine d\'Abyssia Rue des Coraux", '2023-09-02', '2023-09-12', 3500),
          ('La Mission Secrète du Château Hanté', 'Château Hanté de la Lune Noire, Salle des Fantômes', '2023-11-13', '2023-11-23', 7000),
          ('La Conquête du Pic de Glace', 'Montagne Gelée Sommet de Cristal', '2023-12-05', '2023-12-15', 25000),
          ('La Recherche du Livre des Sortilèges', 'Bibliothèque Antique, Rayon des Grimoires',' 2023-10-02', None, 500),
          ('Le Mystère de la Pierre de Lune', 'Forêt de Lumière Clairière des Fées', '2023-08-21', '2023-08-31', 800),
          ('La Quête du Dragon Doré', 'Caverne des Dragons Antre du Gardien', '2023-06-28', None, 250)
    ])
  
  ##Seed Arenes
  mycursor.executemany("""
    INSERT INTO Arenes (name, location, Places, size_m2) 
    VALUES (%s, %s, %s, %s)
    """, [ 
          ('Helicops', '456 Boulevard de la Fantaisie Revopolis', 25, 250),
          ('Sun', '123 Rue des Etoiles Lumiereville Mystica', 5, 70),
          ('Eclair', '789 Avenue des Arc-en-Ciel Feeriqueville', 500, 3000),
          ('Terra', "234 Allée de l\'Aventure Arcadia Légendaville",0,0)
    ])
  
  ##Seed Stores
  mycursor.executemany("""
    INSERT INTO Stores (name, location) 
    VALUES (%s, %s)
    """, [
          ('LumierMart','123 Rue de la Liberté Arc-en-Cielville'),
          ('EcoMonster', '456 Avenue des Songes Luneville'),
          ('MoCouture', '789 Chemin de la Féérie Flottemagie'),
          ('SavSphere', '101 Rue des Nuages Crystallineville'),
          ('MobiliBulle', '234 Allée des Mystères Ensorcelville'),
          ('GalactiGear', "567 Boulevard de l\'Aurore Cielétincell"),
          ('PlanePlantes', "890 Promenade de l\'Enchantement Brumeville"),
          ('MystiMonster', '210 Avenue des Lumières Sylveclaire'),
          ('RobeoMonster', '543 Rue des Étoiles Fleurétoile'),
          ('ArteMonster', '876 Chemin de la Magie Auroreville' )
    ])

  mydb.commit()
