import logging


# TODO: remember to add syslog option to this

def getlogger(logger_name):
    logger = logging.getLogger(logger_name)
    logging.basicConfig(format='%(asctime)s %(levelname)s %(name)s %(message)s',
                        level=logging.DEBUG)
    logger.setLevel(logging.DEBUG)
    return logger