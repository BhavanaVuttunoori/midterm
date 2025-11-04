import logging
import os
from app.calculator_config import Config

log_file = os.path.join(Config.LOG_DIR, "calculator.log")

logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)

class Logger:
    @staticmethod
    def log(message: str):
        logging.info(message)
