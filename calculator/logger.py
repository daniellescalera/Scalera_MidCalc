import logging
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get log level from environment variable, default to INFO
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()

# Configure logging
logging.basicConfig(
    filename="calculator.log",  # Log file
    level=getattr(logging, LOG_LEVEL, logging.INFO),  # Convert string to log level
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# Create logger instance
logger = logging.getLogger(__name__)
