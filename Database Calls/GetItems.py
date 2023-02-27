import sqlite3
    
def Start():
    conn = sqlite3.connect('Database.db')
    cursor = conn.cursor()
# Accepts in integer form
def FlipItemFound(ID):
    Start()
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
    Start()
    cursor.execute(f"SELECT * FROM Items WHERE ItemID = {ID};")
    for item in cursor.fetchall():
        cursor.execute(f"UPDATE Items SET FreeToAll = 1 WHERE ItemID = {ID};")
    conn.commit()
    conn.close()
    
    
# Accepts in integer form
def ItemWithTags(Tag):
    Start()
    cursor.execute(f"SELECT * FROM Items WHERE Tags LIKE '%-{Tag}-%';")
    return (cursor.fetchall())

# Returns 2d List [[Item1], [Item2]]
def GetAllItems():
    Start()
    cursor.execute("SELECT * FROM Items")
    return (cursor.fetchall())

# Accepts 0 or 1 (false or true)
def ItemsWithSecurity(Level):
    Start()
    cursor.execute(f"SELECT * FROM Items WHERE Security = '{Level}';")
    return (cursor.fetchall())
