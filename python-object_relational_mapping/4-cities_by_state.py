#!/usr/bin/python3
# Author: Joana Casallas
""" List all cities from the database hbtn_0e_4_usa """
import sys
import MySQLdb


def main():
    """main function to connect to the database and fetch cities"""
    db = MySQLdb.connect(
        host='localhost',
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3],
        port=3306)

    cur = db.cursor()
    try:
        query = (
            "SELECT c.id, c.name, s.name FROM cities c "
            "LEFT JOIN states s ON c.state_id = s.id "
            "ORDER BY c.id ASC;"
            )
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
