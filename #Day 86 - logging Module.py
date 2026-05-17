#Day 86 - logging Module 
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.debug("This will not show")
logging.info("Day 86 started")
logging.warning("This is a warning")
logging.error("This is an error")