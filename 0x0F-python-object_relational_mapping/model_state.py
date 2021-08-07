#!/usr/bin/python3
"""Is a python file that contains the class definition of a State
and an instance Base = declarative_base()"""

from sqlalchemy import Integer, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.elements import collate

Base = declarative_base()


class State(Base):
    __tablename__ = 'states'
    id = Column(Integer,
                autoincrement=True,
                unique=True,
                nullable=False,
                primary_key=True)

    name = Column(String(128),
                  nullable=False)
