# UTF-8
# Date : January 5th, January
# Margaux Faurie



#Import 
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker, query
from connection import connect, createdb, checkdb
from createtable import createtables
from populate import populate
from models import Battery, Memory
import datetime
import json
import pandas as pd
import matplotlib.pyplot as plt

#Collect info for the connection to MySQL
with open("config.json") as f: #Load data for the configuration
        config = json.load(f)

        username = config["username"]
        password = config["password"]
        host = config["host"]
        port = config["port"]

separation = '-------------------------------------------'

#Name the database
dbname = 'datalog'

#Def useful functions
def CheckDB(dbname):  #Create the database at the beggining of the program
    print(separation)

    if checkdb(dbname) is True: #Create the database if it does not exists

        print('The database does not exist. Set up in process.')
    
        createdb(dbname) #Create the database
        session = connect(dbname) #Connect to the database

        createtables(dbname) #Create the tables
        populate(dbname) #Populate the database
        
        print('Setup ended. Database created.')
        print(separation)
        prgrm = 1
        return prgrm
    
    else: 
        print("Your database already exists.\n")
        
        engine = db.create_engine(f'mysql+pymysql://{username}:{password}@{host}/{dbname}')
        connection = engine.connect() #Reconnect to the database
        
        try:
            Table = int(input('Which table do you want to see ? \n '))
        except ValueError:
            print("The input is not right...\n")
            prgrm = 0
            return prgrm  

        pd.DataFrame(connection.execute("SELECT * FROM {}".format(Table)))

        print('Do you want to delete the tables to run the program anyway ?')
        print('1 = Delete the tables and recreate others.')
        print('2 = Add the new values to the table')
        print('Other integer: do not run the program\n')

        try:
            Choice = int(input('Your choice : '))
        except ValueError:
            print("The input is not right...\n")
            prgrm = 0
            return prgrm


    if Choice == 1:
        prgrm = 1 
        engine = db.create_engine(f'mysql+pymysql://{username}:{password}@{host}/{dbname}')
        connection = engine.connect() #Connect

        session = connect(dbname) #Connect to the database

        #Delete the tables
        query = db.delete(Memory)
        results = connection.execute(query)

        query = db.delete(Battery)
        results = connection.execute(query) 

        populate(dbname) #Populate the database with what we want
        return prgrm

    elif Choice == 2:
        prgrm = 1 
        populate(dbname)
        print("Data was added to the table")
        print(separation)
        return prgrm

    else:    
        prgrm = 0
        print('The program will not run')
        print(separation)
        return prgrm


def ReadTable(dbname, Table):
    engine = db.create_engine(f'mysql+pymysql://{username}:{password}@{host}/{dbname}')
    connection = engine.connect() #Reconnect to the database
    return pd.DataFrame(connection.execute("SELECT * FROM {}".format(Table)))

print(CheckDB(dbname))
print(separation)

print("Memory Table: \n")
ReadTable(dbname, Memory)
print(separation)

print("Battery Table: \n")
ReadTable(dbname, Battery)
print(separation)

graph_table = str(input("Which table do you want to see on a graph ?"))

dataframe = pd.read_sql('SELECT * FROM {}'.Table)
dataframe.plot(x ='time', y='data')
plt.title('Graph of {} by Time'.format(Table))
plt.ylabel('Collected Data')
plt.xlabel('Time in seconds')
plt.savefig('Graph.png')
plt.show()

