# UTF-8
# Date : January 5th, January
# Margaux Faurie

import datetime
from connection import connect
from models import Memory, Battery
import psutil
import datetime

def populate(dbname):
    """populate the table with memory and battery data"""
    session = connect(dbname)

    
    for i in range(10):
        memory_data = psutil.virtual_memory()
        battery_data = psutil.sensors_battery()
        #Populate the memory data
        MemoryData = Memory(Date = datetime.datetime.now(),
                            Total = memory_data.total,
                            Available = memory_data.available,
                            Percent = memory_data.percent,
                            Used = memory_data.used,
                            Free = memory_data.free)
        session.add(MemoryData)

        #Populate the battery data
        BatteryData = Battery(Date = datetime.datetime.now(),
                            Percent = battery_data.percent,
                            Seconds_left = battery_data.secsleft,
                            Power_Plugged = battery_data.power_plugged)
        session.add(BatteryData)

    session.commit()


