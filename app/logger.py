import logging


def setup_logger():
    """
    function for setup logger

    :return: logger
    """
    logger = logging.getLogger("ASYNC_API_PROJECT")
    logger.setLevel(logging.DEBUG)

    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    ch.setFormatter(formatter)

    logger.addHandler(ch)

    return logger


logger = setup_logger()
