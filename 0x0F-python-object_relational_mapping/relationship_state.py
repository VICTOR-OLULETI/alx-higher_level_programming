#!/usr/bin/python3
"""
    This module introduces the model for the State
    class
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """
        This class is created to represent the
        state table
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state')

# State.cities.property.cascade = "all, delete, delete-orphan"
