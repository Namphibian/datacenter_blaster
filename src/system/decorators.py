import functools
import logging

_LOGGER = logging.getLogger(__name__)
_LOGGER.info("Starting decorators uvicorn")


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            _LOGGER.info(f"Executing {func.__name__} with parameters {args}, {kwargs}")
            result = func(*args, **kwargs)
            _LOGGER.info(f"Finished {func.__name__}")
            return result
        except Exception as e:
            _LOGGER.exception(
                f"Exception raised in {func.__name__}. exception: {str(e)}"
            )
            raise e

    return wrapper
