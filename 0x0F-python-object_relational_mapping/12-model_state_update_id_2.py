#!/usr/bin/python3
"""Changes the name of a State object from the database hbtn_0e_6_usa"""

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

    # Query for the State object with id=2 and update its name to "New Mexico"
    state = session.query(State).filter(State.id == 2).first()
    if state:
        state.name = "New Mexico"
        session.commit()
