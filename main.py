from fastapi import FastAPI
from fastapi.responses import FileResponse
import joblib
from research.Model import filepath
from schemas import BankNoteModel
import pandas as pd

app = FastAPI()

model = joblib.load(filename=filepath)

@app.get("/")
def home():

    return FileResponse("templates/index.html")

@app.get("/tools")
def tools():
    return FileResponse("templates/Predict.html")

       


@app.post("/predict")
async def ModelPrediction(data: BankNoteModel):
    input_df = pd.DataFrame([data.model_dump()])
    #model_dump() attribute converts the data into a python dictionary instead of something that could only be read by pydantic
    prediction = model.predict(input_df)
    if prediction[0] == 1:
        result = "Fake Note"
    else:
        result = "Not a Fake Note"

    return {
        "status": "success",
        "prediction": prediction[0],
        "result": result
    }

