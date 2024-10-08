#!/usr/bin/python3
# Author: Joana Casallas
""" List all City objects from the database hbtn_0e_101_usa """
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City
from relationship_state import State
from sqlalchemy.orm import joinedload


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    cities_and_states = session.query(City).options(
        joinedload(City.state)).order_by(City.id).all()

    for city in cities_and_states:
        print(f"{city.id}: {city.name} -> {city.state.name}")

    session.close()
