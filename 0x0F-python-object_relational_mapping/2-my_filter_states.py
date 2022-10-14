#!/usr/bin/python3
"""
    This module takes in an argument and displays
    all values in the states table of the database
    where name matches the argument
"""


import sys
import MySQLdb


def main():
    """
        This func prints the state values
        matched
    """
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_searched = sys.argv[4]
    db = MySQLdb.connect(
            host="localhost", port=3306, passwd=mysql_password,
            db=database_name, user=mysql_username
            )
    r = db.cursor()
    result = """SELECT states.id, name FROM states
                WHERE name = '{}' ORDER BY states.id""".format(state_searched)
    r.execute(result)

    for i in r.fetchall():
        print(i)
    r.close()
    db.close()


if __name__ == "__main__":
    # only to run when not called by import
    main()
