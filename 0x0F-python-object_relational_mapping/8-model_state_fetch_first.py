#!/usr/bin/python3
"""
    This module returs the first state object
    from the specified database.
    command line arguments:
        first-argument: username
        second-argument: password
        third-argument: database_name
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(
                sys.argv[1], sys.argv[2], sys.argv[3]),
            pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    state = session.query(State).order_by(State.id).first()
    if (state is not None):
        print("{}: {}".format(state.id, state.name))
    else:
        print('Nothing')
    session.close()
