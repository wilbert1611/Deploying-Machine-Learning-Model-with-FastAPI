from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import pandas as pd

app = FastAPI()
#Memuat model terbaik Machine Learning yang telah disimpan tadi yaitu XGBoost
with open('XGB.pkl', 'rb') as file:
    pipeline = pickle.load(file)

#Mendefinisikan struktur data input yang diterima oleh API
class ObesityPredictionInput(BaseModel):
    Gender: str
    Age: int
    Height: float
    Weight: float
    family_history_with_overweight: str
    FAVC: str
    FCVC: float
    NCP: float
    CAEC: str
    SMOKE: str
    CH2O: float
    SCC: str
    FAF: float
    TUE: float
    CALC: str
    MTRANS: str

#Endpoint root untuk memberikan pesan
@app.get("/")
def read_root():
    return {"message": "Welcome to the Obesity Prediction API / Wilbert Suwanto"}

#Endpoint untuk melakukan prediksi
@app.post("/predict")
async def predict(input_data: ObesityPredictionInput):
    data = input_data.dict() #Mengonversi input menjadi dictionary
    df = pd.DataFrame([data]) #Mengonversi dictionary menjadi DataFrame

    prediction = pipeline.predict(df) #Melakukan prediksi menggunakan model yang dimuat
    
    prediction = int(prediction[0]) #Mengonversi hasil prediksi menjadi integer
    
    return {"prediction": prediction} #Mengembalikan hasil prediksi
