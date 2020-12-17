# UTF8
# Date: December 17, 2020
# Author: Margaux Faurie

from sqlalchemy import MetaData
from sqlalchemy import Column, Integer, String, Boolean, Table, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlconnection import engine

def createtables(name):
    """Create table for the database"""
    Base = declarative_base()
    engin = engine(name)
    metadata = MetaData(bind = engin)

    memory = Table(
        'memory', metadata,
        Column('id', Integer, primary_key = True),
        Column('Date', String, Nullable = False ),
        Column('Total', Integer, Nullable = True),
        Column('Available', Integer, Nullable = True),
        Column('Percent', Integer, Nullable = True),
        Column('Used', Integer, Nullable = True ),
        Column('Free', Integer, Nullable = True)
    )

    battery = Table(
        'battery', metadata,
        Column('id', Integer, primary_key = True),
        Column('Date', String, Nullable = False),
        Column('Percent', Integer, Nullable = True),
        Column('Seconds_left', Integer, Nullable = True),
        Column('Power_Pluffed', String, Nullable = True)
    )

    #Create all tables
    metadata.create_all(engin)
    return memory, battery
