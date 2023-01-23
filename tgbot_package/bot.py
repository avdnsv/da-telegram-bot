"""This file contains a description about bot and methods"""
import os

import telebot
import httpx

import dadata_package.custom_dadata
import tgbot_package.all_types
from tgbot_package import const

# tests = [1, 2, 3, 'a', 'b', 'c']


def telegram_bot():
    """Bot function"""
    bot = telebot.TeleBot(os.environ['BOT_TOKEN'])

    @bot.message_handler(commands=["start", "help"])
    def start(message):
        bot.send_message(
            message.chat.id, const.HELP_DESCRIPTION, parse_mode='html'
        )

    @bot.message_handler(commands=["points"])
    def points(message):
        bot.send_message(
            message.chat.id, const.POINTS_DESCRIPTION, parse_mode='html'
        )

    # noinspection PyTypeChecker
    @bot.message_handler(content_types=tgbot_package.all_types.AllTypes())
    def message(message):
        if message.text:
            try:
                data = dadata_package.custom_dadata.CustomDadata(
                    os.environ['DADATA_TOKEN'], os.environ['DADATA_SECRET']
                )
                data.dadata_response(message.text)
                bot.send_message(message.chat.id, data.customized_data())
                # bot.send_message(message.chat.id, str(tests))  # for test bot
            except telebot.apihelper.ApiTelegramException as error:
                bot.send_message(message.chat.id, 'Неверный адрес! Попробуйте еще раз.')
            except httpx.HTTPStatusError as error:
                bot.send_message(message.chat.id, 'Сервис недоступен! Попробуйте позже')
            except Exception as error:
                bot.send_message(message.chat.id, 'Ошибка! Попробуйте позже')
        else:
            bot.send_message(message.chat.id, 'Неизвестный адрес! Попробуйте еще раз.')

    bot.polling()
