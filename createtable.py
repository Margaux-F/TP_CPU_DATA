# UTF-8
# Date : January 5th, January
# Margaux Faurie


from sqlalchemy import MetaData
from sqlalchemy import Column, Integer, String, Boolean, Table, ForeignKey, Date
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from connection import engine

def createtables(name):
    """Create table for the database"""
    Base = declarative_base()
    engin = engine(name)
    metadata = MetaData(bind = engin)

    memory = Table(
        'memory', metadata,
        Column('id', Integer, primary_key = True),
        Column('Date', Date, nullable = False ),
        Column('Total', Integer, nullable = True),
        Column('Available', Integer, nullable = True),
        Column('Percent', Integer, nullable = True),
        Column('Used', Integer, nullable = True ),
        Column('Free', Integer, nullable = True)
    )

    battery = Table(
        'battery', metadata,
        Column('id', Integer, primary_key = True),
        Column('Date', Date, nullable = False),
        Column('Percent', Integer, nullable = True),
        Column('Seconds_left', Integer, nullable = True),
        Column('Power_Pluffed', String, nullable = True)
    )

    #Create all tables
    metadata.create_all(engin)
    return memory, battery