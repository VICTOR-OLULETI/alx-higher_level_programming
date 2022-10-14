#!/usr/bin/python3
"""
    This module deletes all State records name
    containing the letter a from the database
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
    session.query(State).\
        filter(State.name.ilike("%a%")).\
        delete(synchronize_session='fetch')
    session.commit()
