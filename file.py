
from logger import Logger


logger = Logger()

def test_log(value: str):
    logger.debug(value)
    logger.info(value)
    logger.error(value)
    print(value)



test_log("asdasdsad")