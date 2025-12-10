import logging
import sys
from datetime import datetime
from typing import Any, Dict


class LoggingManager:
    """
    A centralized logging manager that implements the required logging framework
    for error and performance tracking without user identification.
    """
    
    def __init__(self):
        self.logger = logging.getLogger("textbook_logger")
        self.logger.setLevel(logging.INFO)
        
        # Create console handler with formatting
        if not self.logger.handlers:
            handler = logging.StreamHandler(sys.stdout)
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            )
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)
    
    def log_error(self, message: str, error: Exception = None, **kwargs):
        """
        Log an error without user identification
        """
        log_msg = f"ERROR: {message}"
        if error:
            log_msg += f" - Exception: {str(error)}"
        if kwargs:
            log_msg += f" - Additional info: {kwargs}"
        
        self.logger.error(log_msg)
    
    def log_performance(self, operation: str, duration: float, **kwargs):
        """
        Log performance metrics without user identification
        """
        log_msg = f"PERFORMANCE: Operation '{operation}' took {duration:.4f} seconds"
        if kwargs:
            log_msg += f" - Additional info: {kwargs}"
        
        self.logger.info(log_msg)
    
    def log_info(self, message: str, **kwargs):
        """
        Log general information without user identification
        """
        log_msg = f"INFO: {message}"
        if kwargs:
            log_msg += f" - Additional info: {kwargs}"
        
        self.logger.info(log_msg)


# Global logger instance
logger = LoggingManager()


def get_logger():
    """
    Returns the global logger instance
    """
    return logger