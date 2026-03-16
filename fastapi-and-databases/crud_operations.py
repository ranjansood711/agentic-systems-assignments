from db import engine
from tables import students
from sqlalchemy import insert

def create_student(input_id: int, input_name: str, input_age: int, input_city: str):
    with engine.connect() as conn:
        query = insert(students). values(id= input_id, name= input_name, age= input_age, city = input_city)
        conn.execute(query)
        conn.commit()