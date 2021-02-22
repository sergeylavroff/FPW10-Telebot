import telebot
from config import currency, TOKEN
from extensions import ConvertionException, CurrencyConvertor

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['photo', ])
def say_lmao(message: telebot.types.Message):
    bot.reply_to(message, 'Nice meme XDD')

@bot.message_handler(commands=['values'])
def show_values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in currency.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)

@bot.message_handler(commands=['start', 'help'])
def handle_docs_audio(message):
    bot.send_message(message.chat.id,f'Псс, {message.chat.username}. Как насчет курса валюты?\nЧтобы узнать курс валюты введите\
    <имя валюты из которой переводим> <имя валюты в которую переводим> и количество для перевода. Чтобы ознакомиться со списком валют введите команду values.')

@bot.message_handler(content_types=['text', ])
def responder(message: telebot.types.Message):
    try:
        if len(message.text.split(' ')) != 3:
            raise ConvertionException('Число параметров отлично от трех!')
        base, quote, amount = message.text.split(' ')
        text = f'Цена {amount} {base} в {quote} - {CurrencyConvertor.get_price(base, quote, amount)}'
    except ConvertionException as e:
        bot.reply_to(message, f'Ошибка во введенных данных.\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Ошибка сервера.\n{e}')
    else:
        bot.send_message(message.chat.id, text)


bot.polling(none_stop=True)