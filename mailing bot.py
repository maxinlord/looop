import telebot
import config2
from telebot import types

bot = telebot.TeleBot(config2.TOKEN)

markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
buton1 = types.KeyboardButton('📤новая рассылка')
itembtna = types.KeyboardButton('➕добавить чат')
itembtnb = types.KeyboardButton('➖удалить чат')
itembtnc = types.KeyboardButton('🕒задать время рассылки')
markup1.row(buton1)
markup1.row(itembtna)
markup1.row(itembtnb)
markup1.row(itembtnc)


@bot.message_handler(commands=['start', 'help'])
@bot.edited_message_handler(content_types=['text'])
def welcome(message):
    bot.send_message(message.chat.id,
                     'Здравствуйте вас приветствует бот для рассылки поста по чатам. Нажмите соответствующий пункт меню для создания новой рассылки',
                     reply_markup=markup1)


@bot.message_handler(content_types=['text'])
def otvet(message):
    bot.send_message(message.chat.id, 'Упс... пока ничего нет)')


bot.polling(timeout=60)
