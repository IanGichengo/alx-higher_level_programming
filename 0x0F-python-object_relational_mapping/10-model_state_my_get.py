#!/usr/bin/python3
"""Prints the State object with the name passed as an argument"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # Extract command line arguments
    username, password, database, state_name = sys.argv[1:5]

    # Create engine and session
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            username, password, database
        ), pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query for the State object with the given name
    state = session.query(State).filter(State.name == state_name).first()

    # If state is found, print its id, otherwise print 'Not found'
    if state:
        print(state.id)
    else:
        print("Not found")
