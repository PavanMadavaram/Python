#Day 68 - Logging Helper
import logging

logger = logging.getLogger("app")
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
logger.addHandler(handler)

logger.debug("Debug message")
logger.error("Error occurred")