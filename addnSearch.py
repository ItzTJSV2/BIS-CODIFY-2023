import sqlite3

conn = sqlite3.connect("Database.db")
cursor = conn.cursor()


def addItem(name: str, location: str, imageAdr: str, date: str, tag: list, security: str):
    tag.sort()
    tagStr = "-"
    for i in tag:
        tagStr += str(i) + "-"

    cmd = "INSERT INTO Items (ItemName, Location, DirecImage, DateFound, Tags, Security)"
    val = "VALUES ({}, {}, {}, {}, {}, {})".format(
        name, location, imageAdr, date, tagStr, security)
    cursor.execute(cmd, val)
