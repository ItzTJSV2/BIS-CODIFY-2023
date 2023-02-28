import sqlite3


def Start():
    conn = sqlite3.connect("Database.db")
    cursor = conn.cursor()
    return cursor, conn


# Adds item to the database
def AddItem(name: str, location: int, imageAdr: str, date: str, tags: list, security: int):
    cursor, conn = Start()

    # Manipulate tags list into the form of "-n1-n2-n3-..." where n represents the id of tag
    tagStr = "-"
    for i in tags:
        tagStr += str(i) + "--"

    # Add item to the database
    print(f"{name}, {location}, {imageAdr}, {date}, {tagStr}, {security}")
    cursor.execute(f"INSERT INTO Items (ItemName, Location, DirecImage, DateFound, Tags, Security) VALUES ('{name}', '{location}', '{imageAdr}', '{date}', '{tagStr}', '{security}');")
    conn.commit()
    conn.close()


# Returns 2d List [[Item1], [Item2], ...]
def SearchItem(location: int, date: str, tags: list):
    cursor, conn = Start()

    # Manipulate tags list into the form of ['-n1-', '-n2-;, ...] where n represents the id of tag
    tags = ["-" + str(tag) + "-" for tag in tags]

    # Search any item that contains more than one of the tags
    option = [f"tags LIKE '%{tag}%'" for tag in tags]
    cursor.execute("SELECT * FROM Items WHERE " + " OR ".join(option))
    data = [item + [0] for item in cursor.fetchall()]

    # Assign importance value to each item
    maxImportance = 0
    for item in data:
        # tag - importance: +3
        for tag in tags:
            if item[5].__contains__(tag):
                item[-1] += 3

        # Location - importance: +2
        if item[2] == location:
            item[-1] += 2

        # Date - importance: +1
        if item[4] > date:
            item[-1] += 1

        # Get highest score for running counting sort
        if item[-1] > maxImportance:
            maxImportance = item[-1]

    # Sort the searched data into the order of importance
    search = CountingSort(maxImportance, data)
    return search


def CountingSort(w: int, data: list):
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
        result[index] = item[0:-1]
        counter[val] -= 1

    return result
