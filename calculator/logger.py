import logging
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get log level from environment variable, default to INFO
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()
LOG_FILE = os.getenv("LOG_FILE", "calculator.log")  # Ensure the log file path is set

# Configure logging
logging.basicConfig(
    level=getattr(logging, LOG_LEVEL, logging.INFO),
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, mode='a'),  # ✅ Append mode, ensures logs persist
        logging.StreamHandler()  # ✅ Also log to console
    ],
    force=True  # ✅ Forces immediate log configuration update
)

# Create logger instance
logger = logging.getLogger(__name__)
