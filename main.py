import time
from utils.logger import logger

if __name__ == "__main__":
    counter = 0
    while True:
        logger.info(f"Test log entry {counter}")
        counter += 1
        time.sleep(10)
