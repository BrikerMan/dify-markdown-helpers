import logging
import os

logger = logging.getLogger(__name__)

if os.environ.get("DEBUG"):
    logger.setLevel(logging.DEBUG)
else:
    logger.setLevel(logging.INFO)