#!/usr/bin/env python
# -*- coding: Windows-1251 -*-
import telebot
from telebot import types
import misc
import texts
import teachers
bot = telebot.TeleBot(misc.token)


data = {}


class User:
    group = ""
    kur_gr = ""
    teachers = []
    fd = ""
    specialization = ""
    role = "default"


default = User()


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
    if message.chat.id not in data:
        bot.send_message(message.chat.id, texts.start_message)
        data.update({message.chat.id: default})
    keyboard = types.InlineKeyboardMarkup()
    button_1 = types.InlineKeyboardButton(text="10МИ", callback_data="10")
    button_2 = types.InlineKeyboardButton(text="11МИ", callback_data="11")
    button_3 = types.InlineKeyboardButton(text="Абитуриент", callback_data="12")
    button_4 = types.InlineKeyboardButton(text="Другое", callback_data="13")
    keyboard.add(button_1, button_2, button_3, button_4)
    bot.send_message(message.chat.id, "Выберите ваш класс:", reply_markup=keyboard)


@bot.message_handler(commands=["help"])
def choose_class(message):
    bot.send_message(message.chat.id, texts.help_message)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    # Первая регистрация
    if "10" <= call.data <= "13":
        data[call.message.chat.id].group = call.data
        if call.data == "11" or call.data == "10":
            choose_group(call.message)
        else:
            bot.delete_message(call.message.chat.id, call.message.message_id)
    elif "1" <= call.data <= "5":
        data[call.message.chat.id].kur_gr = call.data
        bot.delete_message(call.message.chat.id, call.message.message_id)
    # ФД
    if call.data == "bi":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, "https://www.hse.ru/ba/bi/")
    elif call.data == "phys_fak":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, "https://physics.hse.ru/")
    elif call.data == "math":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, "https://math.hse.ru/")
    elif call.data == "fkn":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, "https://cs.hse.ru/")
    elif call.data == "kompling":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, "https://www.hse.ru/ma/ling/")
    elif call.data == "miem":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, "https://miem.hse.ru/")
    # Учителя
    if call.data in teachers.subjects:
        bot.delete_message(call.message.chat.id, call.message.message_id)
        keyboard = types.InlineKeyboardMarkup()
        for teacher in teachers.subjects[call.data]:
            keyboard.add(types.InlineKeyboardButton(text=teacher, callback_data=teacher))
        bot.send_message(call.message.chat.id, "Выберите учителя:", reply_markup=keyboard)
    if call.data in teachers.all_teachers:
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, call.data)
    # TBC


@bot.message_handler(commands=["ivr"])
def ivr_info(message):
    bot.send_message(message.chat.id, texts.ivr_info)


@bot.message_handler(commands=["places"])
def places_info(message):
    bot.send_message(message.chat.id, texts.places_info)


@bot.message_handler(commands=["groups"])
def ivr_info(message):
    bot.send_message(message.chat.id, texts.groups_info)


@bot.message_handler(commands=["fd"])
def fd_info(message):
    keyboard = types.InlineKeyboardMarkup()
    button_1 = types.InlineKeyboardButton(text="ФизФак", callback_data="phys_fak")
    button_2 = types.InlineKeyboardButton(text="Матфак", callback_data="math")
    button_3 = types.InlineKeyboardButton(text="ФКН", callback_data="fkn")
    button_4 = types.InlineKeyboardButton(text="МИЭМ", callback_data="miem")
    button_5 = types.InlineKeyboardButton(text="КомпЛинг", callback_data="kompling")
    button_6 = types.InlineKeyboardButton(text="БИ", callback_data="bi")
    keyboard.add(button_1, button_2, button_3, button_4, button_5, button_6)
    bot.send_message(message.chat.id, "Выберите интересующий вас факультетский день:", reply_markup=keyboard)


@bot.message_handler(commands=["teachers"])
def teacher_info(message):
    keyboard = types.InlineKeyboardMarkup()
    for subject in teachers.subjects:
        button = types.InlineKeyboardButton(text=subject, callback_data=subject)
        keyboard.add(button)
    bot.send_message(message.chat.id, "Выберите предмет:", reply_markup=keyboard)


if __name__ == '__main__':
    bot.polling(none_stop=True)

