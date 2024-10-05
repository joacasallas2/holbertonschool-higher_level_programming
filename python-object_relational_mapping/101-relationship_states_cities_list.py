#!/usr/bin/python3
# Author: Joana Casallas
""" List all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa """
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State, Base
from relationship_city import City

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    states_and_cities = session.query(State).outerjoin(
        City).order_by(State.id, City.id).all()
    for state in states_and_cities:
        print(f"{state.id}: {state.name}")
        for city in state.cities:
            print(f"\t{city.id}: {city.name}")

    session.close()
