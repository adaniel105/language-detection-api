from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path
from pydantic import BaseModel
from models.model import prediction_pipeline


app = FastAPI(
    title="LangDetect",
    description="A Language Detection Webservice API",
    version="1.0.0",
)

template_folder = Path(__file__).resolve(strict=True).parent / "templates"
templates = Jinja2Templates(directory=str(template_folder))


class Prediction(BaseModel):
    language: str


@app.get("/", response_class=HTMLResponse)
async def index(request: Request, prediction: str = ""):
    return templates.TemplateResponse(
        "index.html", {"request": request, "prediction": prediction}
    )


@app.post("/predict")
async def predict(request: Request, prediction_text: str = Form()):
    preds = prediction_pipeline(prediction_text)
    return templates.TemplateResponse(
        "index.html", {"request": request, "prediction": preds}
    )
