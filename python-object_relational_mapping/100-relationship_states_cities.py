#!/usr/bin/python3
# Author: joana Casallas
""" Add the State object “Louisiana” to the database hbtn_0e_6_usa """
from sys import argv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from relationship_state import State, Base
from relationship_city import City


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    california = State(name='California')
    sanFrancisco = City(name="San Francisco", state=california)
    session.add(california)
    session.commit()
    session.close()
