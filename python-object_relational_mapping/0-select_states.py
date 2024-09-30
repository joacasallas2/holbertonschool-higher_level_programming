#!/usr/bin/python3
# Author: Joana Casallas
""" List all states from the database hbtn_0e_0_usa """
import MySQLdb

db = MySQLdb.connect(
    host="localhost",
    user="root", password="",
    database="hbtn_0e_0_usa")
cur = db.cursor()
query = "SELECT * FROM states ORDER BY id ASC;"
cur.execute(query)
results = cur.fetchall()
for row in results:
    print(row)

cur.close()
db.close()
