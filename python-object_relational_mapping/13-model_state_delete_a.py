#!/usr/bin/python3
# Author: Joana Casallas
""" Delete all State objects with a name containing
the letter a from the database hbtn_0e_6_usa """
from sys import argv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    names_with_a = session.query(State).filter(State.name.like('%a%')).all()
    for state in names_with_a:
        session.delete(state)
    session.commit()
    session.close()
