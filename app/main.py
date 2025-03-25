from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# from app.langchain_agent import create_agent

app = FastAPI()

@app.get("/")
def root():
    return {"Hello": "World"}
