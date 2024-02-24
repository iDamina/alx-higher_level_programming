#!/usr/bin/python3
"""  a script that lists all states with a name starting with N """
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    current = db.cursor()
    current.execute("SELECT * FROM states WHERE name
                    like BINARY 'N%' ORDER BY states.id")
    rows = current.fetchall()
    for row in rows:
        print(row)
    current.close()
    db.close()
