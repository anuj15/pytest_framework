import logging
import pytest

@pytest.fixture
def logger():
    # Configure the logger
    logger = logging.getLogger("pytest_logger")
    logger.setLevel(logging.DEBUG)

    # Create console handler and set level to debug
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    # Create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)

    # Add handler to the logger
    if not logger.hasHandlers():
        logger.addHandler(console_handler)

    yield logger

    # Clean up handlers to avoid duplicate logs
    logger.handlers.clear()
