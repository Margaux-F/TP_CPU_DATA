# UTF-8
# Author : Margaux Faurie
# 17 décembre 2020

"""
Collect data from CPU
---------
Test
"""

import psutil
import datetime

memory_data = psutil.virtual_memory()
battery_data = psutil.sensors_battery()

#General data
print("Memory data : ", memory_data)
print("Battery data : ", battery_data)


#Memory data
date = datetime.datetime.now()
total = memory_data.total

print(memory_data.total)


