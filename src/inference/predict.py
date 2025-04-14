import pandas as pd
from joblib import load

model = load("models/model.pkl")

def predict(data: dict):
    df = pd.DataFrame([data])
    return model.predict(df)[0]
