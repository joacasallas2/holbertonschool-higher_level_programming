#!/usr/bin/python3
# Author: Joana Casallas
"""takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument"""
import sys
import MySQLdb


def main():
    """ main function to connect to the database and fetch states """
    db = MySQLdb.connect(
        host='localhost',
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306)

    cur = db.cursor()

    try:
        query = ("SELECT * FROM states WHERE name = %s")
        cur.execute(query, (sys.argv[4], ))
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
