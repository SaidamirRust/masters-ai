import logging
import os

def setup_logger(name, log_file="app.log", level=logging.INFO):
    """Set up a logger with the specified name and log file."""
    log_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(log_formatter)
    file_handler.setLevel(level)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_formatter)
    console_handler.setLevel(level)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

# Initialize a global logger
LOGGER = setup_logger("RestaurantInsights")

# Example usage
LOGGER.info("Logger initialized successfully.")