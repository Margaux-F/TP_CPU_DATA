# UTF-8
# Date : December 17, 2020
# Margaux Faurie

import sqlalchemy as db
from sqlalchemy.orm import sessionmaker, query
from sqlconnection import connect, createdb, checkdb
from sqlcreatetable import createtables
from sqlpopulate import populate
from sqlmodels import Battery
from sqlmodels import Memory
import datetime
import json
import pandas as pd


print('\n\n----------------------------------------------------')
print("Setup in progress. Please wait.")
print('----------------------------------------------------\n')

dbname = 'DATALOGCPU' #Name the database


with open("config.json") as f: #Load data for the configuration
        config = json.load(f)

        username = config["username"]
        password = config["password"]
        host = config["host"]
        port = config["port"]


def Checkdb(dbname):  
    createdb(dbname) #Create the database
    session = connect(dbname) #Connect to the database

    createtables(dbname) #Create the tables
    populate(dbname) #Populate the database

    return 'database available'


Checkdb(dbname)

# Reads the database

engine = db.create_engine(f'mysql+pymysql://{username}:{password}@{host}/{dbname}')
connection = engine.connect() #Reconnect to the database

def printtable(connection, tablename): # Def a function that print a database using pandas
    return pd.DataFrame(connection.execute("SELECT * FROM {}".format(tablename)))


print("Table selected :\n")
tablename = str(input('Which table do you want to see (memory, battery) : \n'))
print(printtable(connection, tablename))
print('\n----------------------------------------------------\n')

