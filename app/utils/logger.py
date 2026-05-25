from loguru import logger

logger.add(
    "app.log",
    rotation="5 MB",
    level="INFO"
)