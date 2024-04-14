#!/usr/bin/python3
"""
Module for connecting to MySQL database and querying the cities table
"""

import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name FROM cities \
                JOIN states ON cities.state_id = states.id \
                WHERE states.name=%s ORDER BY cities.id ASC", (sys.argv[4],))
    rows = cur.fetchall()
    for row in rows:
        print("{}, ".format(row[1]), end="")
    print("")
    cur.close()
    db.close()
