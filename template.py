import os
from pathlib import Path
import logging
import sys

logger_filepath = os.path.join("logs", "logging.log")
os.makedirs("logs", exist_ok=True)

logger = logging.basicConfig(level=logging.INFO, 
                    format='[%(asctime)s]: %(filename)s - %(message)s',
                    handlers=[
                        logging.FileHandler(logger_filepath),
                        logging.StreamHandler(sys.stdout)]
                        )

list_of_files = [
    "research/trail.ipynb",
    "src/__init__.py",
    "src/ml_project/logger.py",
    "src/ml_project/__init__.py",
    "requirements.txt",
    "setup.py",
    "research/Model.py",
    "research/__init__.py",
    "schemas.py",
    "templates/index.html",
    "templates/'Predict.html",
    "vercel.json"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"creating directory {filedir} for the {filename}.")
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"creating {filepath} successful.")

    else:
        logging.info(f"{filepath} already exists.")