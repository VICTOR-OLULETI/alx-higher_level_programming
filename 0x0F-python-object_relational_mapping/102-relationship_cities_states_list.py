#!/usr/bin/python3
"""
    This module lists all city object from the
    database
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session


if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(
                sys.argv[1], sys.argv[2], sys.argv[3]),
            pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    q = session.query(City).order_by(City.id).all()
    for city in q:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))
    session.close()
