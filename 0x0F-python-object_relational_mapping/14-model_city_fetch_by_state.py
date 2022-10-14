#!/usr/bin/python3
"""
    This module returns the state name, city id
    and city name
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from model_city import City
from sqlalchemy.orm import Session
from sqlalchemy import distinct

if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(
                sys.argv[1], sys.argv[2], sys.argv[3]),
            pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    q = session.query(State.name, City.id, City.name).\
        order_by(City.id).\
        filter(City.state_id == State.id).all()
    for i in q:
        print("{}: ({}) {}".format(i[0], i[1], i[2]))
    session.close()
