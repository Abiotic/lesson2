"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
import ephem
import settings
import datetime
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')

'''
PROXY = {
    'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn',
        'password': 'python'
    }
}
'''

planets = {'Mercury' : ephem.Mercury(),
           'Venus' : ephem.Venus(),
           'Mars' : ephem.Mars(),
           'Jupiter' : ephem.Jupiter(),
           'Saturn' : ephem.Saturn(),
           'Uranus' : ephem.Uranus(),
           'Neptune' : ephem.Neptune(),
           'Pluto' : ephem.Pluto()}

def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(text)

def constellation_process(update, context):
    planet = update.message.text.split(' ')[-1]
    planets[planet].compute(datetime.datetime.now())
    update.message.reply_text(ephem.constellation(planets[planet]))

# сделала так, потому что на совзовне подслушала про вариант реализации с if  


def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", constellation_process))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
