#!/usr/bin/python3
# Author: Joana Casallas
""" This module contains the class definition of a State
and an instance Base = declarative_base() """
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


Base = declarative_base()


class State(Base):
    """Class State mapped to the states table"""
    __tablename__ = 'states'

    id = Column(Integer(), primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", back_populates="state", cascade="delete, all")
