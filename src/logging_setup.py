# Log file setup and rotation
import logging
from logging.handlers import RotatingFileHandler

# Setup logging with rotation
def setup_logger(log_file="traffic_log.txt", max_bytes=1024 * 1024, backup_count=5):
    """
    Configure a logger with rotating file handler.
    - log_file: Name of the log file.
    - max_bytes: Maximum file size before rotation (default: 1MB).
    - backup_count: Number of backup files to keep.
    """
    handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
    logging.basicConfig(
        handlers=[handler],
        level=logging.INFO,
        format="%(asctime)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    return logging.getLogger(__name__)
