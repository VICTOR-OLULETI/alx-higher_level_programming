#!/usr/bin/python3
"""
    This module lists all cities from
    the database hbtn_0e_4_usa
"""


import sys
import MySQLdb


def main():
    """
        This function prints out the cities from
        the database
    """
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    db = MySQLdb.connect(
            host="localhost", port=3306, passwd=mysql_password,
            db=database_name, user=mysql_username
            )
    r = db.cursor()
    r.execute("""SELECT ROW_NUMBER() OVER () AS row_num,
                cities.name, states.name FROM cities
                JOIN states ON state_id = states.id
                ORDER BY cities.id""")

    for i in r.fetchall():
        print(i)


if __name__ == "__main__":
    # only to run when not called import
    main()
