import logging

import cv2
from pyzbar.pyzbar import decode
import telebot

from config import BOT_TOKEN
import db

logger = logging.getLogger(__name__)

bot = telebot.TeleBot(BOT_TOKEN)
FILE_IMAGE = "images/image.jpg"


def handle_photo(file):
    with open(FILE_IMAGE, 'wb') as new_file:
        new_file.write(file)
    try:
        image = cv2.imread(FILE_IMAGE)
        decoded_objects = decode(image)

        if decoded_objects:
            qr_data = decoded_objects[0].data.decode("utf-8")
            db.save_qr_data_to_db(qr_data)
            logger.info('Successful photo processing')
            return True
        else:
            logger.warning('Unsuccessful photo processing')
            return False
    except Exception as e:
        logger.error(e)
        return False


def start_bot():

    @bot.message_handler(content_types=['photo'])
    def message_handler(message):
        file_info = bot.get_file(message.photo[-1].file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        processed = handle_photo(downloaded_file)
        logger.info('Send message to user')
        if processed:
            bot.reply_to(message, "Готово!")
        else:
            bot.reply_to(message, "QR код не обнаружен")

    bot.infinity_polling(skip_pending=True)



if __name__ == "__main__":
    try:
        logger.warning('Start the Bot')
        db.check_database()
        start_bot()
    except KeyboardInterrupt:
        logger.warning('Closing the Bot')
    except Exception as e:
        logger.error(e)
    finally:
        db.conn.close()
        logger.warning('Bot is closed')
