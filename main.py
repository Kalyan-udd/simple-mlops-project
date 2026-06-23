from fastapi import FastAPI
from fastapi.responses import FileResponse
import joblib
from schemas import BankNoteModel
from ml_project.logger import logger
from pandas import DataFrame


app = FastAPI()

filepath = "artifacts/trained_model.joblib"

model = joblib.load(filename=filepath)

@app.get("/")
def home():
    logger.info("Home page is active...!")
    return FileResponse("templates/index.html")

@app.get("/tools")
def tools():
    logger.info("tools page is active..!")
    return FileResponse("templates/Predict.html")

@app.post("/predict")
async def ModelPrediction(data: BankNoteModel):
    try:
        input_df = DataFrame([data.model_dump()])
        #model_dump() attribute converts the data into a python dictionary instead of something that could only be read by pydantic
        prediction = model.predict(input_df)
        if prediction[0] >= 0.5:
            result = "Fake Note"
        else:
            result = "Not a Fake Note"
        logger.info("server responded successfully")
        return {
            "status": "success",
            "prediction": int(prediction[0]),
            "result": result
        }
    except Exception as e:
        logger.info(f"Error occurred - {e}")

