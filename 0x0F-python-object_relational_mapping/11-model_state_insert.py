#!/usr/bin/python3
"""Adds the State object "Louisiana" to the database hbtn_0e_6_usa"""

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

    # Create the State object for Louisiana and add it to the session
    louisiana = State(name="Louisiana")
    session.add(louisiana)
    session.commit()

    # Print the new state's id
    print(louisiana.id)
