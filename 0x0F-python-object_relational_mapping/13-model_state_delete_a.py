#!/usr/bin/python3
""" Deletes all State objects with a name containing the letter 'a' """

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # Extract command line arguments
    username, password, database = sys.argv[1:4]

    # Create engine and session
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            username, password, database
        ), pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query for all State objects with a name containing the letter "a"
    states_with_a = session.query(State).filter(State.name.like('%a%')).all()
    for state in states_with_a:
        session.delete(state)
    session.commit()
