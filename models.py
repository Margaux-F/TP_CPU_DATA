# UTF-8
# Date : January 5th, January
# Margaux Faurie


from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy import DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from connection import connect

session = connect('DATALOGCPU')

Base = declarative_base()


class Memory(Base):
    'Class to handle memory data '
    __tablename__ = "memory"
    id = Column(Integer, primary_key=True)
    Date = Column(String, nullable = True)
    Total = Column(Integer, nullable = True)
    Available = Column(Integer, nullable = True)
    Percent = Column(Float, nullable = True)
    Used = Column(Integer, nullable = True)
    Free = Column(Integer, nullable = True)

class Battery(Base):
    'Class to handle battery data'
    __tablename__ = "battery"
    id = Column(Integer, primary_key = True)
    Date = Column(String, nullable = True)
    Percent = Column(Integer, nullable = True)
    Seconds_left = Column(Integer, nullable = True)
    Power_Plugged = Column(String, nullable = True)
    
