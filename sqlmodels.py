# UTF8
# Date: December 17, 2020
# Author: Margaux Faurie

from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy import DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlconnection import connect

session = connect('DATALOGCPU')

Base = declarative_base()


class Memory(Base):
    'Class to handle memory data '
    __tablename__ = "memory"
    id = Column(Integer, primary_key=True),
    Date = Column(String, nullable = True),
    Total = Column(Integer, Nullable = True),
    Available = Column(Integer, Nullable = True),
    Percent = Column(float, Nullable = True),
    Used = Column(Integer, Nullable = True ),
    Free = Column(Integer, Nullable = True)

class Battery(Base):
    'Class to handle battery data'
    __tablename__ = "battery"
    id = Column(Integer, primary_key = True),
    Date = Column(String, Nullable = False),
    Percent = Column(Integer, Nullable = True),
    Seconds_left = Column(Integer, Nullable = True),
    Power_Plugged = Column(String, Nullable = True)
    
