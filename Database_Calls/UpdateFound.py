import sqlite3
from GetItems import *
from datetime import datetime

conn = sqlite3.connect('Database.db')
cursor = conn.cursor()

current_time = datetime.today()

for item in GetAllItems():
    time_diff = datetime.today() - datetime.strptime(item[4], "%Y-%m-%d")
    if (time_diff >= 20):
        ItemIsNowFree(item[0])
        

conn.commit()
conn.close()
