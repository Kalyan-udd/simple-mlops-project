from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import joblib
from ml_project.logger import logger
from pathlib import Path


dataframe = pd.read_csv("research/BankNote_Authentication.csv")

features = ["variance", "skewness", "curtosis", "entropy"]
X = dataframe[features]
y = dataframe['class']

X_train, X_test, y_train, y_test = train_test_split(X,y, random_state=42, test_size=0.3)



model = GradientBoostingClassifier()

model.fit(X_train, y_train)

filepath = "artifacts/trained_model.joblib"

filepath = Path(filepath)

logger.info(f"saving the model to file - {filepath}")

joblib.dump(model, filename=filepath)

logger.info(f"serialisation successful. saved to {filepath}")
