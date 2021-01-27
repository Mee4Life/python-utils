import logging

def getLogger(fileName) -> logging: 
    # create logger
    logger = logging.getLogger(fileName)
    logger.setLevel(logging.ERROR)
    ch  = logging.FileHandler('logs/' + fileName + '.log')
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger