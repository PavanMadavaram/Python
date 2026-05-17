#Day 86 - Logging Helper
import logging

logger = logging.getLogger("day86")
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler()
formatter = logging.Formatter("%(levelname)s: %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

logger.debug("Debug message")
logger.info("Info message")
logger.error("Error message")