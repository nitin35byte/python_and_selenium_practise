import inspect
import logging


class BaseClass:
    def test_loggingDemo(self):
        loggerName=inspect.stack()[1][3]
        logger=logging.getLogger(__name__)

        filehandler= logging.FileHandler('logfile.log')

        formatter=logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)

        logger.setLevel(logging.INFO)
        return logger
        # logger.debug("A debug statement is execute")
        # logger.info("Information Statement")
        # logger.warning("Something is in warning mode")
        # logger.error("A major error ahs happen")
        # logger.critical("Critical issue")