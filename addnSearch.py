import sqlite3


def start():
    conn = sqlite3.connect("Database.db")
    cursor = conn.cursor()
    return cursor, conn


# Adds item to the database
def addItem(name: str, location: str, imageAdr: str, date: str, tags: list, security: str):
    cursor, conn = start()

    # Manipulate tags list into the form of "-n1-n2-n3-..." where n represents the id of tag
    tagStr = "-"
    for i in tags:
        tagStr += str(i) + "-"

    # Add item to the database
    data = f"{name}, {location}, {imageAdr}, {date}, {tagStr}, {str(security)}"
    print(data)
    # cursor.execute(f"INSERT INTO Items (ItemName, Location, DirecImage, DateFound, Tags, Security) VALUES ('{data});")
    cursor.execute(f"INSERT INTO Items (ItemName, Location, DirecImage, DateFound, Tags, Security) VALUES ('{name}', '{location}', '{imageAdr}', '{date}', '{tagStr}', '{str(security)}');")
    conn.commit()
    conn.close()


# Returns 2d List [[Item1], [Item2], ...]
def searchItem(types:list, properties: list, location: int):
    cursor, conn = start()

    # Type is the tag that has highest priority -- When searching, the item MUST include one of the types given
    cmd = "SELECT * FROM Items WHERE Found = 0 "
    if types != []:
        # Search any item that contains more than one of the tags
        condition = " OR ".join([f"Type = {tag}" for tag in types])
        cmd += f"AND ({condition}) "

    if properties != []:
        # Manipulate tags list into the form of ['-n1-', '-n2-;, ...] where n represents the id of tag
        properties = [f"-{tag}-" for tag in properties]

        # Search any item that contains more than one of the tags
        condition = " OR ".join([f"Property LIKE '%{tag}%'" for tag in properties])
        cmd += f"AND ({condition}) "

    # location == 0 represents Location isn't given
    elif location:
        condition = "Location = " + str(location)
        cmd += f"AND {condition}"

    cmd += "BY ItemID DESC LIMIT 50"
    print(cmd)
    data = [item + [0] for item in cursor.fetchall()]

    # Assign importance value to each item
    maxImportance = 0
    for item in data:
        # tag - importance: +2
        for tag in properties:
            if item[5].__contains__(tag):
                item[-1] += 2

        # Location - importance: +1
        if item[2] == location:
            item[-1] += 1

        # Get highest score for running counting sort
        if item[-1] > maxImportance:
            maxImportance = item[-1]

    # Sort the searched data into the order of importance
    search = countingSort(maxImportance, data)
    return search


def countingSort(w: int, data: list):
    # Count number of items in the specific importance level
    counter = [0] * w + [0]
    for item in data:
        val = w - item[-1]
        counter[val] += 1

    # Manipulate the counter to get index of items in the room
    counter[0] -= 1
    for i in range(w):
        counter[i + 1] += counter[i]

    # insert items into the new list
    result = [0] * len(data)
    for item in data:
        val = w - item[-1]
        index = counter[val]
        result[index] = item[:-1]
        counter[val] -= 1

    return result
