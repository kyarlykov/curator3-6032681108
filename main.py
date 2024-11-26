from telebot import TeleBot

bot = TeleBot('7825752611:AAH3KM99KamEXTpzfk4qRzgPTTTjDKD5TCQ')


@bot.message_handler(commands=['start'])
def chunga(message):
    bot.send_message(message.chat.id, 'привет, ты сегодня очень красивая(ый) ')

@bot.message_handler(commands=['miu'])
def cfity(message):
    bot.send_message(message.chat.id, 'https://ru.pinterest.com/pin/66005950783408863/')

bot.infinity_polling()