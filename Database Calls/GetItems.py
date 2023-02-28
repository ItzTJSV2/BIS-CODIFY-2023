import sqlite3
from addnSearch import *
    
def Start():
    conn = sqlite3.connect('Database.db')
    cursor = conn.cursor()
    return conn, cursor
# Accepts in integer form
def FlipItemFound(ID):
    conn, cursor = Start()
    cursor.execute(f"SELECT * FROM Items WHERE ItemID = {ID};")
    for item in cursor.fetchall():
        if item[6] == 0:
            cursor.execute(f"UPDATE Items SET Found = 1 WHERE ItemID = {ID};")
        elif item[6] == 1:
            cursor.execute(f"UPDATE Items SET Found = 0 WHERE ItemID = {ID};")
    conn.commit()
    conn.close()
    
    
# Accepts in integer form
def ItemIsNowFree(ID):
    conn, cursor = Start()
    cursor.execute(f"SELECT * FROM Items WHERE ItemID = {ID};")
    for item in cursor.fetchall():
        cursor.execute(f"UPDATE Items SET FreeToAll = 1 WHERE ItemID = {ID};")
    conn.commit()
    conn.close()
    
    
# Accepts in integer form
def ItemWithTags(Tag):
    conn, cursor = Start()
    cursor.execute(f"SELECT * FROM Items WHERE Tags LIKE '%-{Tag}-%';")
    return (cursor.fetchall())

# Returns 2d List [[Item1], [Item2]]
def GetAllItems():
    conn, cursor = Start()
    cursor.execute("SELECT * FROM Items")
    return (cursor.fetchall())

# Accepts 0 or 1 (false or true)
def ItemsWithSecurity(Level):
    conn, cursor = Start()
    cursor.execute(f"SELECT * FROM Items WHERE Security = '{Level}';")
    return (cursor.fetchall())

# Accepts 0 or 1 (false or true)
def ItemsWithFound(Found):
    conn, cursor = Start()
    cursor.execute(f"SELECT * FROM Items WHERE Found = '{Found}';")
    return (cursor.fetchall())