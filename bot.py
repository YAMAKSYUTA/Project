#!/usr/bin/env python
# -*- coding: Windows-1251 -*-
import telebot
from telebot import types
import misc
import texts
bot = telebot.TeleBot(misc.token)


def choose_group(message):
    bot.delete_message(message.chat.id, message.message_id)
    keyboard = types.InlineKeyboardMarkup()
    button_1 = types.InlineKeyboardButton(text="МИ1", callback_data="1")
    button_2 = types.InlineKeyboardButton(text="МИ2", callback_data="2")
    button_3 = types.InlineKeyboardButton(text="МИ3", callback_data="3")
    button_4 = types.InlineKeyboardButton(text="МИ4", callback_data="4")
    button_5 = types.InlineKeyboardButton(text="МИ5", callback_data="5")
    keyboard.add(button_1, button_2, button_3, button_4, button_5)
    bot.send_message(message.chat.id, "Выберите кураторскую группу:", reply_markup=keyboard)


@bot.message_handler(commands=["start", "changeclass"])
def choose_class(message):
    bot.send_message(message.chat.id, texts.start_message)
    keyboard = types.InlineKeyboardMarkup()
    button_1 = types.InlineKeyboardButton(text="10МИ", callback_data="10")
    button_2 = types.InlineKeyboardButton(text="11МИ", callback_data="11")
    button_3 = types.InlineKeyboardButton(text="Абитуриент", callback_data="12")
    button_4 = types.InlineKeyboardButton(text="Другое", callback_data="13")
    keyboard.add(button_1, button_2, button_3, button_4)
    bot.send_message(message.chat.id, "Выберите ваш класс:", reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if "10" <= call.data <= "13":
        if call.data == "11" or call.data == "10":
            choose_group(call.message)
    elif "1" <= call.data <= "5":
        bot.delete_message(call.message.chat.id, call.message.message_id)


if __name__ == '__main__':
    bot.polling(none_stop=True)

