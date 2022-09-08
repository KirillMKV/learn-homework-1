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
from datetime import datetime

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')

list_of_planets = [] # getting list of planets names from ephem
for i in range(8):
    list_of_planets.append(ephem._libastro.builtin_planets()[i][2].lower())

def greet_user(update, context): # greetting message after /start command
    text = f"Hello, user!"
    print(text)
    update.message.reply_text(text)

def define_constellation(update, planet_name): # define constallation name for planet selected by user
  planet = getattr(ephem, planet_name.capitalize())(ephem.now())
  update.message.reply_text(str(ephem.constellation(planet)[1]))


def talk_to_me(update, context): 
    user_text = update.message.text.lower()
    if user_text not in list_of_planets: # CHECK: is user's text name of the planet?
      update.message.reply_text("Are you sure this is planet's name?")
      update.message.reply_text("Please, input planet's name from Solar System")
    else:
      update.message.reply_text(define_constellation(update, user_text)) 
    #update.message.reply_text(text)

def get_planet_name(update, context):
  update.message.reply_text('Input planet name')

def main():
    mybot = Updater("5457682533:AAETPwnjJ40znXNbMwKSIiezpOt2XvLvCIE", use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", get_planet_name))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
