#pip install fastapi pydantic uvicorn
#uvicorn main:app --reload

from fastapi import FastAPI, HTTPException
from typing import Optional

app = FastAPI()

@app.get("/search")
def search(name: Optional[str] = None, age: Optional[int] = None):
    # FastAPI automatically converts this dictionary into a JSON response
    return {
        "name": name,
        "age": age
    }