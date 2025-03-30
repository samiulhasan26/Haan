# Telegram Cloth Remover Bot

import telebot
from telebot import types

API_TOKEN = 8042953822:AAGWcVMYxS0CRDlWtdN8dDLfLjLPuEfDSC4
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to the Cloth Remover Bot! Send me a photo to remove the background.")

@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    file_info = bot.get_file(message.photo[-1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)

    with open("received_photo.jpg", 'wb') as new_file:
        new_file.write(downloaded_file)

    # Here you would add the code to process the image and remove the background
    # For example, using OpenCV or any other image processing library

    # After processing, send the modified image back
    with open("processed_photo.jpg", 'rb') as processed_file:
        bot.send_photo(message.chat.id, processed_file)

bot.polling()