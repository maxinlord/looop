import telebot
from telebot import types


bot = telebot.TeleBot('1398078863:AAGiPfSDLqnsDoxmFo9dAJXm4y2_zXsMbBg')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn0 = types.KeyboardButton('Обновить')
    btn1 = types.KeyboardButton('🐱')
    btn2 = types.KeyboardButton('🎁')
    btn3 = types.KeyboardButton('⭐️')
    btn4 = types.KeyboardButton('👼')
    markup.add(btn1, btn2, btn3, btn4, btn0)
    send_mess = f"<b>Привет Настёна) </b>\nВыбери одну из кнопок"
    bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)



@bot.message_handler(content_types=['text'])
def all(message):
        bot.send_message(-1001376078813,f"@{message.from_user.username} - {message.from_user.first_name}({message.from_user.last_name})\nОтправил текст: \n\n{message.text}",parse_mode='html')
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
    if message.text == '👼':
        bot.send_message(message.chat.id, 'Бог тебя БЕЗМЕРНО любит 🤗')
        bot.send_message(message.chat.id, 'Не забывай это 😉')
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIgTF-A4KHdMgVT2CcrGLJmtKRFKIVZAAINAANwGuYapepbBWhY1XcbBA')
    if message.text == 'Обновить':
        bot.send_message(message.chat.id,'Нажми на 👉🏻 /start, чтобы обновить')


bot.polling(none_stop=True)
