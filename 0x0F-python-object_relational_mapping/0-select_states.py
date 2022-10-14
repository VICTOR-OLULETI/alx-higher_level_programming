#!/usr/bin/python3
"""
    This module connect to the database
    and return the states contained in it
"""

import sys
import MySQLdb


mysql_username = sys.argv[1]
mysql_password = sys.argv[2]
database_name = sys.argv[3]
"""
engine = create_engine(
        "mysql+mysqldb://"+mysql_username + ":"
        + mysql_password+"@localhost:3306/" + database_name
        )
"""
db = MySQLdb.connect(
        host="localhost", port=3306, passwd=mysql_password,
        db=database_name, user=mysql_username
        )
r = db.cursor()
r.execute("""SELECT states.id, name FROM states
        ORDER BY states.id""")
for i in r.fetchall():
    print(i)
r.close()
db.close()
