#!/usr/bin/python3
"""a python file similar to model_state.py named model_city.py, City class"""

from sqlachemy.ext.declarative import declarative_base
from sqlachemy import Column, Integer, String, ForeignKey
from sqlachemy.orm import relationship

Base = declarative_base()


class City(Base):
    """Class City"""

    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True,
                primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
