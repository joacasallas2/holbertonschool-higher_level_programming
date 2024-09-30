#!/usr/bin/python3
# Author: Joana Casallas
""" List all states from the database hbtn_0e_0_usa """
import MySQLdb


def main():
    """ main function to connect to the database and fetch states."""
    db = MySQLdb.connect(
        host="localhost",
        user="root",
        password="",
        database="hbtn_0e_0_usa")

    cur = db.cursor()

    try:
        query = "SELECT * FROM states ORDER BY id ASC;"
        cur.execute(query)
        results = cur.fetchall()
        for row in results:
            print(row)
    except MySQLdb.Error as e:
        print(f"Error: {e}")
    finally:
        cur.close()
        db.close()


if __name__ == "__main__":
    main()
