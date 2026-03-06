# uvicorn file_name:fastapi_object
# uvicorn file_name:fastapi_object --reload (Auto restart when changes saved)

from fastapi import FastAPI, HTTPException
import json

app = FastAPI()

# localhost:8000/hello
@app.get("/hello")
def say_hello():
    return "Hello Everyone, nice to meet!"

# localhost:8000/bye
@app.get("/bye")
def say_bye():
    return "Bye Everyone!"

def load_students_data():
    with open('students.json', 'r'):
        return 

#Get all the students
# localhost:8000/students
@app.get("/students")
def get_all_students():
    return load_students_data()


@app.get("/students/{student_id}")
def get_student_with_id(student_id: str):
    data = load_students_data()
    
    if student_id not in data:
        raise HTTPException(status_code=404, detail="Student with given id not found.")
    
    return data(student_id)