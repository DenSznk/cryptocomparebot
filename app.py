import telebot
from telebot import types
from config import TOKEN, currencies_names
from exceptions import ConvertingExceptions, CurrencyConvertor

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'], )
def creating_buttons(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("🪙 Available currencies")
    item2 = types.KeyboardButton("📍 Navigation")
    markup.add(item1, item2)
    bot.send_message(message.chat.id, "Hi i'm a bot, i can convert currency.\nLet's start!".format(message.from_user),
                     reply_markup=markup)


@bot.message_handler(content_types='text')
def check_action(message):
    if message.chat.type == 'private':
        if message.text == "📍 Navigation":
            bot.send_message(message.chat.id, "To get started, enter the command in the following format:\n"
                                              "currencies name what currency to transfer amount \n")
        elif message.text == "🪙 Available currencies":
            text = "Available currencies:"
            for name in currencies_names.keys():
                text = '\n'.join((text, name))
            bot.send_message(message.chat.id, text)
        elif message.text:

            try:
                values = message.text.split(' ')
                if len(values) != 3:
                    raise ConvertingExceptions('Invalid input format.')

                quote, base, amount = values
                total_base = CurrencyConvertor.convert(quote, base, amount)
            except ConvertingExceptions as e:
                bot.reply_to(message, f'User error.\n{e}')
            except Exception as e:
                bot.reply_to(message, f'Failed to process command.\n{e}')
            else:
                text = f'Price {amount} {quote} in {base} - {total_base}'

                bot.send_message(message.chat.id, text)


bot.polling()
