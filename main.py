import telebot
from telebot import types

bot = telebot.TeleBot('1398078863:AAGiPfSDLqnsDoxmFo9dAJXm4y2_zXsMbBg')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    btn1 = types.KeyboardButton('🐱')
    btn2 = types.KeyboardButton('🎁')
    btn3 = types.KeyboardButton('⭐️')
    markup.add(btn1, btn2, btn3, )
    send_mess = f"<b>Привет Настёна) </b>\nВыбери одну из кнопок"
    bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)
    if message.text == '🐱':
        bot.send_message(message.chat.id, 'Ты НЕПОВТОРИМАЯ')
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIgLF-AwXMT0bKSF28uqA06fiT3g0J_AAL3AANWnb0KC3IkHUj0DTAbBA')


@bot.message_handler(content_types=['text'])
def all(message):
    if message.text == '🐱':
        bot.send_message(message.chat.id, 'Ты НЕПОВТОРИМАЯ')
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIgLF-AwXMT0bKSF28uqA06fiT3g0J_AAL3AANWnb0KC3IkHUj0DTAbBA')
    if message.text == '🎁':
        bot.send_message(message.chat.id, 'Ты ПОДАРОК для меня')
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIgP1-AxsFUjpH_7OE2DFs03e3dpcK_AAJGBAACa8TKCl9-OHTeCINwGwQ')
    if message.text == '⭐️':
        bot.send_message(message.chat.id, 'Ты ЗВЕЗДА и пусть мне кто-то поспорит еще 👊🏻')
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIgQl-AyDq0BGXwNr4bEvCftSAE1tc5AAJ_DgACqAgvCDkkmchEn1qxGwQ')
        bot.send_message(message.chat.id, 'Это я ,кстати, смотрю на тебя))👆🏻')


bot.polling(none_stop=True)
