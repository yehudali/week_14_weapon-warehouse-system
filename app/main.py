from typing import Annotated
from fastapi import FastAPI, File, UploadFile
import uvicorn
import pandas as pd
import json

from servic import processing_data
from db import init_databes


app = FastAPI()

@app.post("/upload")
async def upload_file(file: UploadFile):
    df = pd.read_csv(file.file)
    df = processing_data(df)
    init_databes()
    return {"filename": df.info()}



if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
