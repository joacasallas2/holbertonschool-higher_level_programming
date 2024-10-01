#!/usr/bin/python3
# Author: Joana casallas
""" lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa"""
import sys
import MySQLdb


def main():
    """ main function to connect to the database and fetch states """
    db = MySQLdb.connect(
        host='localhost',
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3],
        port=3306)

    cur = db.cursor()

    try:
        query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC;"
        cur.execute(query)
        results = cur.fetchall()
        for row in results:
            print(row)
    except MySQLdb.Error as e:
        print(f"Error: {e}")
    finally:
        cur.close()
        db.close()


if __name__ == '__main__':
    main()
