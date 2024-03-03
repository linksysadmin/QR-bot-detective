import os
import logging
from logging.handlers import TimedRotatingFileHandler

from dotenv import load_dotenv

logger = logging.getLogger(__name__)

# Environment

load_dotenv('.env')

BOT_TOKEN = os.getenv('BOT_TOKEN')
DB_NAME = os.getenv('DB_NAME')

if not DB_NAME or not BOT_TOKEN:
    ERROR = "Ошибка: Не удалось загрузить переменные DB_NAME или BOT_TOKEN из .env"
    logger.error(ERROR)
    raise ValueError(ERROR)

# Logging

handler = TimedRotatingFileHandler('logs/log.log', when='D', interval=10)
handler.setFormatter(logging.Formatter('%(name)s %(asctime)s - %(levelname)s - %(message)s'))

logging.basicConfig(handlers=[handler],
                    format="%(name)s %(asctime)s - %(levelname)s - %(message)s",
                    datefmt='%m.%d.%Y %H:%M:%S',
                    level=logging.INFO)

