from logger import Logger

logger = Logger()


def test(value: str):
    logger.debug(value)
    logger.info(value)
    logger.error(value)
    print(value)


test('test')

def one_mode_def(value):
    logger.error(value)


one_mode_def('Другая функция')