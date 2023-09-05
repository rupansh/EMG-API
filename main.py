from typing import Annotated, List, Tuple
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

class EmgData(BaseModel):
    emg: Tuple[int, int, int, int, int] 

app = FastAPI()

@app.post("/glove")
def glove(emg: EmgData):
    return {"fingers": [1, 1, 1, 1, 1]}
