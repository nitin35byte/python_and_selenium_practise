from logging import getLogger
import logging
def test_loggingDemo():
    logger=logging.getLogger(__name__)

    filehandler= logging.FileHandler('logfile.log')

    formatter=logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
    filehandler.setFormatter(formatter)
    logger.addHandler(filehandler)

    logger.setLevel(logging.INFO)
    logger.debug("A debug statement is execute")
    logger.info("Information Statement")
    logger.warning("Something is in warning mode")
    logger.error("A major error ahs happen")
    logger.critical("Critical issue")


# logger = logging.getLogger(__name__)
# filehandler= logging.FileHandler()
#
# formatter= logging.Formatter("")
# filehandler.setFormatter(formatter)
# logger.addHandler(filehandler)
# logger.setLevel(logging.INFO)


##call getlogger
##2.  handler- we need to give name of the file
##3. formatter
##4. now i will pass formater to handler
## now i will pass formatter to handler
## i will set lwver

