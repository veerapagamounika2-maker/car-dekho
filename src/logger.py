import logging
import os
from datetime import datetime

# Create a folder to store logs
LOG_DIR = "logs"
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# Create log file with current date and time
LOG_FILE = f"log_{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.log"
LOG_PATH = os.path.join(LOG_DIR, LOG_FILE)

# Configure logging settings
logging.basicConfig(
    filename=LOG_PATH,
    level=logging.INFO,  # You can change this to DEBUG, WARNING, ERROR if needed
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# Create a logger object
logger = logging.getLogger()

# Example usage
if __name__ == "__main__":
    logger.info("Application started.")
    logger.warning("This is a warning message.")
    logger.error("This is an error message.")
    logger.info("Application finished.")