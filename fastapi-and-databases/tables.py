from db import engine
from sqlalchemy import MetaData, Table, Column, Integer, String, CheckConstraint

metadata = MetaData()

students = Table(
    'students',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50), nullable=False), 
    Column('age', Integer, CheckConstraint('age >= 18'), nullable=False),
    Column('city', String(50), nullable=True)
)

def create_tables():
    metadata.create_all(engine)
