#!/usr/bin/python3
"""
This module connect to the database
and return the states contained in it
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import MySQLdb
from sqlalchemy import select

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
# Session = sessionmaker(bind=engine)
# session = Session()
# Base = declarative_base()
# Base.metadata.create_all(engine)
# conn = engine.connect()
# trans = conn.begin()
# r = conn.execute("select states.id, name from states order by states.id")
# r = conn.execute(s).fetchall()
# for i in r:
#    print(i)
# conn.close()
# result = session.query(states.id, states.name).all()
# for i in result:
#    print(i)
# s = session.scalars(select(states.c.id)).first()
# print(s)
r = db.cursor()
r.execute("""SELECT states.id, name FROM states
        ORDER BY states.id""")
for i in r.fetchall():
    print(i)
