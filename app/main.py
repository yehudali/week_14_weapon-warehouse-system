from typing import Annotated
from fastapi import FastAPI, File, UploadFile
import uvicorn
import pandas as pd
import json

from servic import processing_data
from db import init_databes, insert_df_to_db


app = FastAPI()

@app.post("/upload")
async def upload_file(file: UploadFile):
    df = pd.read_csv(file.file)
    df = processing_data(df)
    init_databes()
    respons = insert_df_to_db(df)
    inserted = len(df)
    if respons:
        return { 
  "status": respons, 
  "inserted_records": inserted
    }



if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
