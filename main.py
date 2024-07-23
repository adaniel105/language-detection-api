from fastapi import FastAPI
from pydantic import BaseModel
from models.model import prediction_pipeline



app = FastAPI()


class Prediction(BaseModel):
  language : str


@app.get("/")
async def index():
  return {"Health Check" : "OK"}


@app.post("/predict", response_model=Prediction)
async def Predict(language: str):
  preds = prediction_pipeline(language)
  return {"language" : language}





if __name__ == "__main__":
  import uvicorn
  uvicorn.run(app, host="127.0.0.1", port=8080)