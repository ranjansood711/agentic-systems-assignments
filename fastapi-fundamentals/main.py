from fastapi import FastAPI, HTTPException
import json

app = FastAPI()

@app.get("/search")