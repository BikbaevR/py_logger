from logger import Logger

logger = Logger()


def some_func(value):
    logger.info(value)
    return value


some_func('example')
