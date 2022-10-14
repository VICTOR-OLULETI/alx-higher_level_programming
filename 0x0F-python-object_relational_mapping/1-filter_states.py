#!/usr/bin/python3
"""
    This module lists all states with name
    starting with N
"""


import sys
import MySQLdb


def main():
    """
        This function prints out all states
        starting with N
    """
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    db = MySQLdb.connect(
            host="localhost", port=3306, passwd=mysql_password,
            db=database_name, user=mysql_username
            )
    r = db.cursor()
    r.execute("""SELECT states.id, states.name FROM states
            WHERE BINARY states.name LIKE 'N%'""")
    for i in r.fetchall():
        print(i)


if __name__ == "__main__":
    # only to run when not called by import
    main()
