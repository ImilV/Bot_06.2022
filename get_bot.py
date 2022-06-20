import telebot, wikipedia, re

bot = telebot.TeleBot('5579234330:AAHXkEDn5ebPnkoQy7AyTp0S5Bc-MMLkWwg')
keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('Привет', 'Пока', 'Ты мой лучший друг')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне! Я так рад!', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет, мой друг')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Пока, мой друг')
    elif message.text.lower() == 'ты мой лучший друг':
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEFFHVirzLRaTSfZJFUeNDAol6Q14IqjgACGxUAAqqCiUh54P9cqGLH0yQE')

@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)

bot.polling()
