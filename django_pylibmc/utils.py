import functools
import logging

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.WARNING)


def catcher(func):
    """Wrapper to catch exceptions and log them."""

    # preserve function metadata
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            print(f"Running {func.__name__}")
            return func(*args, **kwargs)
        except Exception as e:
            logger.warning("Error occured while executing %s: %s", func.__name__, e)
            return False


def make_and_validate_key(self, key, version=None):
    """Helper to make and validate keys."""
    print(f"Validation of key: {key}")
    key = self.make_key(key, version=version)
    self.validate_key(key)
    return key
