import sys
import os
import mysql.connector
from dotenv import load_dotenv

from src.function.creation import create_database
from src.function.seed_no_fk import seed_no_fk
from src.function.seed_fk import seed_fk
from src.function.delete_tables import delete_tables
from src.function.destroy_database import destroy_database

from src.queries.queries import monster_catch
from src.queries.queries import monster_type
from src.queries.queries import monster_trainers
from src.queries.queries import monster_sale
from src.queries.queries import stores_ca
from src.queries.queries import quests_participe
from src.queries.queries import events
from src.queries.queries import monster_feu
from src.queries.queries import especes_monster

from src.queries.queries_perso import xp_trainers
from src.queries.queries_perso import quest_monster
from src.queries.queries_perso import arene_info
from src.queries.queries_perso import quest_price
from src.queries.queries_perso import monster_weight


from src.etape4.pagination import pagination
from src.etape4.views import view_quest
from src.etape4.views import view_events
from src.etape4.monster_type import call_procedure_monster_type
from src.etape4.monster_update import call_update_monster

from src.bonus.location import location
from src.bonus.deplicate import duplicate_equipment






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

######------------- INFO -------------######
def info():
  print("""
    MMMM   MMMM    OOO     NN   NN    SSSSSS    TTTTTTTT  EEEEEEE   RRRRRR     MMMM   MMMM    OOO     NN   NN
    MM MM MM MM   OO  OO   NNN  NN  SS      SS     TT     EEE       RR   RR    MM MM MM MM   OO  OO   NNN  NN
    MM  MMM  MM  OO    OO  NN N NN    SSS          TT     EEEEEE    RRRRRR     MM  MMM  MM  OO    OO  NN N NN
    MM   M   MM  OO    OO  NN  NNN       SS        TT     EEEEEE    RR  RR     MM   M   MM  OO    OO  NN  NNN
    MM       MM   OO  OO   NN   NN   SS     SS     TT     EEE       RR   RR    MM       MM   OO  OO   NN   NN
    MM       MM    OOO     NN   NN     SSSSSS      TT     EEEEEEE   RR    RR   MM       MM    OOO     NN   NN
 _______________________________________________________________________________________________________________   
|  Création de la DB:                                                                                           |
|  python3 Montsermon.py <-flage>                                                                               |
|                        -create    créer la base de données                                                    |
|                        -seed      alimenter la base de données                                                |
|                                                                                                               |
|  Utilisation des différents flages:                                                                           |
|  python3 Montsermon.py <-flage>                                                                               |
|                        -req_lead  lance tout les requete imposer par le leader                                |
|                        -req_perso       lance des requette supplementaire autre de celle imposer par le leader|
|                        -pagination      Pour limiter l'affichage des resulatats                               |
|                        -view_quest      pour créer un view de la tables Quest nommée StatistiqueMonsterQuete  |
|                        -view_events     pour créer un view de la tables Events nommée StatistiqueEvenement    |
|                        -type_monster    pour afficher les monster solen leur type choisi par le leader        |
|                        -update_monster  pour mettre à jour un monstre                                         |
|                        -location        afficher tout les adresse des tout le jeu                             |
|                        -duplicate       duplique les 3 dernier items de la tables equipment de façon desca    |
|                        -delete    supprime la base de donnée si besoins                                       |
|                        -req <nom_de_requette> lance une seul requette                                         |
|                               monster_catch                                                                   |
|                               monster_type                                                                    |
|                               monster_trainers                                                                |
|                               monster_sale                                                                    |
|                               stores_ca                                                                       |
|                               quests_participe                                                                |
|                               events                                                                          |
|                               monster_feu                                                                     |
|                               especes_monster                                                                 |
 ---------------------------------------------------------------------------------------------------------------
            """)
  
######------------- SEED DATABASE -------------######
def seed_database():
  seed_no_fk()
  seed_fk()
  
######------------- SEED DATABASE -------------######
def delete_database():
  delete_tables()
  destroy_database()
  
######------------- Query Lancher -------------######
def query(flage):
  if flage == "monster_catch":
    monster_catch()
  elif flage == 'monster_type':
    monster_type()
  elif flage == 'monster_trainers':
    monster_trainers()
  elif flage == 'monster_sale':
    monster_sale()
  elif flage == 'stores_ca':
    stores_ca()
  elif flage == 'quests_participe':
    quests_participe()
  elif flage == 'events':
    events()
  elif flage == 'monster_feu':
    monster_feu()
  elif flage == 'especes_monster':
    especes_monster()
    
######------------- Lancher ALL Querys  -------------######
def query_all():
    monster_catch()
    monster_type()
    monster_trainers()
    monster_sale()
    stores_ca()
    quests_participe()
    events()
    monster_feu()
    especes_monster()

######------------- Lancher PERSONAL Querys  -------------######
def query_perso():
  xp_trainers()
  quest_monster()
  arene_info()
  quest_price()
  monster_weight()
    
    
    

def database():
  if len(sys.argv) < 2:
      print("Aucun argument fourni.")
      return
  
  command_map = {
      "help": info,
      "-create": create_database,
      "-seed": seed_database,
      "-delete": delete_database,
      "-req": query,
      "-req_lead": query_all,
      "-req_perso": query_perso,
      "-pagination": pagination,
      "-view_quest": view_quest,
      "-view_events": view_events,
      "-type_monster": call_procedure_monster_type,
      "-update_monster": call_update_monster,
      "-location":location,
      "-duplicate":duplicate_equipment
  }

  arg = sys.argv[1]
  if arg in command_map:
    if arg == "-req" and len(sys.argv) > 2:
        command_map[arg](sys.argv[2])
    else:
        command_map[arg]()
  else:
    print(f"Argument inconnu: {arg}")

database()

