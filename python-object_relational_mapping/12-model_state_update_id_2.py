#!/usr/bin/python3
# Author: joana Casallas
"""Change the name of a State object from the database hbtn_0e_6_usa"""
from sys import argv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import State


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    state_to_change_name = session.query(State).filter_by(id=2).first()
    state_to_change_name.name = 'New Mexico'
    session.commit()
