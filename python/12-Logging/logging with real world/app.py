import logging

## Configure logging settings
logging.basicConfig(
    level = logging.DEBUG,
    format = '%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
) 

logger = logging.getLogger("ArithmeicApp")

def add(a, b):
    result = a+b
    logger.debug(f"Adding {a} + {b} = {result}")
    return result

def substract(a, b):
    result = a-b
    logger.debug(f"Substracting {a} - {b} = {result} ")
    return result

def multiply(a, b):
    result = a*b
    logger.debug(f"Multiplying {a} * {b} = {result} ")
    return result

def divide(a, b):
    try:
        result = a/b
        logger.debug(f"Dividing {a} / {b} = {result} ")
        return result
    except ZeroDivisionError:
        logger.error("Division by zero error")
        return None

add(10, 5)
substract(10, 5)
multiply(10, 5)
divide(10, 5)
divide(10, 0)