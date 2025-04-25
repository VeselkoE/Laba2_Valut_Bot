import telebot
from API_token import all_key, MY_TOKEN
from extensions import APIException, ConverterValue

bot = telebot.TeleBot(MY_TOKEN)


# Процедура start_help с командами start и help используется, чтобы была возможность увидеть инструкцию ввода и узнать
# команду, с помощью которой, можно узнать доступные валюты
@bot.message_handler(commands=['start', 'help'])
def start_help(message):
    text = 'Добрый день!\n' \
           'Для того чтобы начать работать вам необходимо ввести команды в следующем порядке разделяя все пробелом: \n' \
           '<имя валюты, цену которой он хочет узнать>\
           <имя валюты, в которой надо узнать цену первой валюты> <количество первой валюты> \n' \
           'Для того чтобы увидеть список всех доступных валют введите команду /values\n' \
           'При переводе выполняяется округление до двух знаков после запятой с округлением'
    bot.reply_to(message, text)


# Процедура values_all с командой value используется чтобы узнать доступные валюты
@bot.message_handler(commands=['values'])
def values_all(message):
    text = 'В даннный момент доступна следующая валюта'
    for key in all_key.keys():
        text += f'\n {key}'
    bot.reply_to(message, text)


# Процедура convertor используется для того чтобы перевести одну валюту в другую с указанным кол-во Так же в
# процедуре convertor используется команда "capitalize()" чтобы введеное значение всегда начиналось записывать с
# заглавной буквы.
@bot.message_handler(content_types=['text', ])
def convertor(message):
    try:
        values_all = message.text.split(' ')
        if len(values_all) != 3:
            raise APIException('Кол-во использованных переменных не соответствует условиям.')

        quote, base, amount = values_all
        total_base = ConverterValue.get_price(quote.capitalize(), base.capitalize(), amount)
    except APIException as e:
        bot.reply_to(message, f'Ошибка пользователя\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        # в итоговом значение используется округление до двух знаков после запятой
        text = f'Цена {amount} {quote.capitalize()} в {base.capitalize()} = {"%.2f" % total_base}'
        bot.send_message(message.chat.id, text)


bot.polling()#None_stop=True)
