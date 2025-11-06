import logging
from logging.handlers import TimedRotatingFileHandler
import os
from datetime import datetime
import sys

def setup_logger(name: str, log_dir: str = "./logs", backup_days: int = 7):
    """ 
    Setup a logger that writes to both console and rotating log files.
    Log files are timestamped and rotated daily.
    """
    os.makedirs(log_dir, exist_ok=True)

    # Timestamped filename
    log_filename = os.path.join(log_dir, f"{name}.log")

    # Create logger
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # File handler: rotate at midnight
    file_handler = TimedRotatingFileHandler(
        log_filename,     # base filename
        when="midnight",  # rotate at midnight
        interval=1,       # every day
        backupCount=0,    # 0 means **keep all old log files**
        encoding="utf-8"
    )
    file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(file_formatter)

    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_formatter = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
    console_handler.setFormatter(console_formatter)

    # Add handlers if not already added
    if not logger.handlers:
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger

logger = setup_logger('bot')