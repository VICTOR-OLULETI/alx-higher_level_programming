#!/usr/bin/python3
"""
    This module adds a new object to the State
    and City class
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
    california = State(name="California")
    san = City(name="San Francisco")
    california.cities.append(san)
    session.add_all([california, san])
    session.commit()
    session.close()
