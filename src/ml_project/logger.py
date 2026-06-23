import logging
import os
import sys


file_dir = "logs"
filepath = os.path.join(file_dir, "logging.log")

logger = logging.getLogger("SimpleMLOpsProjectLogger")
logger.setLevel(logging.INFO)

formatter = logging.Formatter("[%(asctime)s]: [%(filename)s: %(lineno)d] - %(message)s")

if not logger.handlers:
    file_handler = logging.FileHandler(filepath)
    file_handler.setFormatter(formatter)

    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    logger.propagate = False