#!/usr/bin/python3
# Author: Joana casallas
""" This module contains the class definition of City
and an instance Base = declarative_base() """
from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base


class City(Base):
    """Class City mapped to the cities table"""
    __tablename__ = 'cities'

    id = Column(Integer(), primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer(), ForeignKey(
        'states.id', ondelete='CASCADE'), nullable=False)
