import logging
import os
import sys


file_dir = "logs"
filepath = os.path.join(file_dir, "running_logs.log")

logger = logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s]: %(message)s",
    handlers=[
        logging.FileHandler(filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("SimpleMLOpsProjectLogger")