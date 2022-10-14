#!/usr/bin/python3
"""
    This module takes in 4 arguments and displays
    all cities of a state give by the user
"""


import sys
import MySQLdb


def main():
    """
        This func prints out the cities in
        a given state
    """
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state = sys.argv[4]
    db = MySQLdb.connect(
            host="localhost", port=3306, passwd=mysql_password,
            db=database_name, user=mysql_username
            )
    r = db.cursor()
    r.execute("""SELECT cities.name FROM cities
                JOIN states ON state_id = states.id
                WHERE states.name = %s""", (state,))

    result = ''
    for i in r.fetchall():
        result += i[0] + ', '

    print(result[:-2])
    r.close()
    db.close()


if __name__ == "__main__":
    main()
