#!/usr/bin/python3
""" takes in an argument and displays all values """
import MySQLdb
import sys


if __name__ == "__main__":
    # Retrieve command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create a cursor object
    cur = db.cursor()

    # Construct the SQL query with user input
    query = "SELECT * FROM states WHERE name=%s ORDER BY id ASC"

    # Execute the SQL query with the state name as parameter
    cur.execute(query, (state_name,))

    # Fetch all rows returned by the query
    rows = cur.fetchall()

    # Print the results
    for row in rows:
        print(row)

    # Close the cursor and database connections
    cur.close()
    db.close()
