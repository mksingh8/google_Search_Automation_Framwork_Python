import inspect
import logging


class LogGen:
    @staticmethod
    def log():
        logging.basicConfig(filename="/"
                                     "/Logs/test_log.log", format='%(asctime)s: %(levelname)s: %(name)s: %(message)s '
                                                                  ': %(lineno)s', level=logging.INFO)
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        return logger

#
# logger = LogGen.log()
# logger.info("printing log message")
