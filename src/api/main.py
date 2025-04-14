from fastapi import FastAPI
from pydantic import BaseModel
from src.inference.predict import predict

app = FastAPI()

class InputData(BaseModel):
    feature1: float
    feature2: float
    # Adicione mais features conforme seu dataset

@app.post("/predict")
def get_prediction(data: InputData):
    pred = predict(data.dict())
    return {"prediction": pred}
