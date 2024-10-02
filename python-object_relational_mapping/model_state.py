#!/usr/bin/python3
# Author: Joana Casallas
""" This module contains the class definition of a State
and an instance Base = declarative_base() """
import sys
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
Base = declarative_base()
Base.metadata.create_all(engine)


class State(Base):
    """Class State"""
    __tablename__ = 'states'

    id = Column(Integer(), primary_key=True)
    name = Column(String(128), nullable=False)
