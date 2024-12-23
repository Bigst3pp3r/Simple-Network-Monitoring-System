# Log file setup and rotation
# logger_setup.py
import logging
from logging.handlers import RotatingFileHandler

def setup_logging(log_file, max_bytes, backup_count):
    handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
    logging.basicConfig(
        handlers=[handler],
        level=logging.INFO,
        format="%(asctime)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
