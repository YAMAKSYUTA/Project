#!/usr/bin/env python
# -*- coding: Windows-1251 -*-
import telebot
from telebot import types
import misc
import texts
import teachers
import re
import json
bot = telebot.TeleBot(misc.token)
data = {}


class User:
    group = ""
    kur_gr = ""
    fd = ""
    specialization = ""
    dop_subj = ""
    cnt_for_reg = 1
    announce = 1
    subjects = {
        "Русский язык": "",
        "Математика": "",
        "Иностранный язык": "",
        "Литература": "",
        "Физика": "",
        "ТОК": "",
        "Теоретическая информатика": "",
        "Программирование": "",
        "Базовая информатика": "",
        "Пользовательский курс": "",
        "Физкультура": "",
        "История": ""
    }


default = User()
moderators = {}


def another_timetable(message):
    keyboard = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text="Учебный план", callback_data="other_0")
    button2 = types.InlineKeyboardButton(text="Расписание группы", callback_data="other_1")
    keyboard.add(button1, button2)
    bot.send_message(message.chat.id, text="Что вы хотите увидеть?", reply_markup=keyboard)


def one_day_timetable(message):
    keyboard = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text="Понедельник", callback_data="day_Понедельник")
    button2 = types.InlineKeyboardButton(text="Вторник", callback_data="day_Вторник")
    button3 = types.InlineKeyboardButton(text="Среда", callback_data="day_Среда")
    button4 = types.InlineKeyboardButton(text="Пятница", callback_data="day_Пятница")
    button5 = types.InlineKeyboardButton(text="Суббота", callback_data="day_Суббота")
    keyboard.add(button1, button2, button3, button4, button5)
    bot.send_message(message.chat.id, "Выберите день недели:", reply_markup=keyboard)


def choose_teachers(message, cnt):
    keyboard = types.InlineKeyboardMarkup()
    for teacher in teachers.subjects[teachers.subjects_names[cnt]]:
        keyboard.add(types.InlineKeyboardButton(text=teacher, callback_data="teacher_{0}".format(teacher)))
    bot.send_message(message.chat.id, "Выберите вашего учителя по предмету {0}:".format(teachers.subjects_names[cnt]),
                     reply_markup=keyboard)


def choose_profile_subject(message):
    keyboard = types.InlineKeyboardMarkup()
    button_1 = types.InlineKeyboardButton(text="Физика", callback_data="physics_prof")
    button_2 = types.InlineKeyboardButton(text="Информатика", callback_data="inf_prof")
    keyboard.add(button_1, button_2)
    bot.send_message(message.chat.id, "Выберите профильный предмет:", reply_markup=keyboard)


def edit_profile_subject(message):
    keyboard = types.InlineKeyboardMarkup()
    button_1 = types.InlineKeyboardButton(text="Физика", callback_data="e_sub_physics_prof")
    button_2 = types.InlineKeyboardButton(text="Информатика", callback_data="e_sub_inf_prof")
    keyboard.add(button_1, button_2)
    bot.send_message(message.chat.id, "Выберите профильный предмет:", reply_markup=keyboard)


def choose_fd(message):
    keyboard = types.InlineKeyboardMarkup()
    button_1 = types.InlineKeyboardButton(text="ФизФак", callback_data="ch_Физфак")
    button_2 = types.InlineKeyboardButton(text="Матфак", callback_data="ch_Матфак")
    button_3 = types.InlineKeyboardButton(text="ФКН", callback_data="ch_ФКН")
    button_4 = types.InlineKeyboardButton(text="МИЭМ", callback_data="ch_МИЭМ")
    button_5 = types.InlineKeyboardButton(text="КомпЛинг", callback_data="ch_КомпЛинг")
    button_6 = types.InlineKeyboardButton(text="БИ", callback_data="ch_БИ")
    button_7 = types.InlineKeyboardButton(text="Нет фд", callback_data="ch_Нет ФД")
    keyboard.add(button_1, button_2, button_3, button_4, button_5, button_6, button_7)
    bot.send_message(message.chat.id, "Выберите факультетский день:", reply_markup=keyboard)


def edit_fd(message):
    keyboard = types.InlineKeyboardMarkup()
    button_1 = types.InlineKeyboardButton(text="ФизФак", callback_data="e_fd_Физфак")
    button_2 = types.InlineKeyboardButton(text="Матфак", callback_data="e_fd_Матфак")
    button_3 = types.InlineKeyboardButton(text="ФКН", callback_data="e_fd_ФКН")
    button_4 = types.InlineKeyboardButton(text="МИЭМ", callback_data="e_fd_МИЭМ")
    button_5 = types.InlineKeyboardButton(text="КомпЛинг", callback_data="e_fd_КомпЛинг")
    button_6 = types.InlineKeyboardButton(text="БИ", callback_data="e_fd_БИ")
    button_7 = types.InlineKeyboardButton(text="Ещё не выбрал", callback_data="e_fd_Нет ФД")
    keyboard.add(button_1, button_2, button_3, button_4, button_5, button_6, button_7)
    bot.send_message(message.chat.id, "Выберите факультетский день:", reply_markup=keyboard)


def choose_var(message):
    keyboard = types.InlineKeyboardMarkup()
    button_1 = types.InlineKeyboardButton(text="ФизПрак", callback_data="var_ФизПрак")
    button_2 = types.InlineKeyboardButton(text="Практикум Python", callback_data="var_Практикум Python")
    button_3 = types.InlineKeyboardButton(text="Пратикум C++", callback_data="var_Пратикум C++")
    button_4 = types.InlineKeyboardButton(text="КомпЛинг", callback_data="var_КомпЛинг")
    button_5 = types.InlineKeyboardButton(text="Обществознание", callback_data="var_Обществознание")
    button_6 = types.InlineKeyboardButton(text="Инженерия", callback_data="var_Инженерия")
    keyboard.add(button_1, button_2, button_3, button_4, button_5, button_6)
    bot.send_message(message.chat.id, "Выберите вариативный предмет:", reply_markup=keyboard)


def edit_var(message):
    keyboard = types.InlineKeyboardMarkup()
    button_1 = types.InlineKeyboardButton(text="ФизПрак", callback_data="evar_ФизПрак")
    button_2 = types.InlineKeyboardButton(text="Практикум Python", callback_data="evar_Практикум Python")
    button_3 = types.InlineKeyboardButton(text="Пратикум C++", callback_data="evar_Пратикум C++")
    button_4 = types.InlineKeyboardButton(text="КомпЛинг", callback_data="evar_КомпЛинг")
    button_5 = types.InlineKeyboardButton(text="Обществознание", callback_data="evar_Обществознание")
    button_6 = types.InlineKeyboardButton(text="Инженерия", callback_data="evar_Инженерия")
    keyboard.add(button_1, button_2, button_3, button_4, button_5, button_6)
    bot.send_message(message.chat.id, "Выберите вариативный предмет:", reply_markup=keyboard)


def choose_group(message):
    keyboard = types.InlineKeyboardMarkup()
    for i in range(1, 6):
        if i != 5 or data[message.chat.id].group == "11":
            keyboard.add(types.InlineKeyboardButton(text=str(i), callback_data="type{0}".format(i)))
    bot.send_message(message.chat.id, "Выберите кураторскую группу:", reply_markup=keyboard)


def choose_one_subject(message, subject):
    keyboard = types.InlineKeyboardMarkup()
    for teacher in teachers.subjects[subject]:
        index = teachers.subjects[subject].index(teacher)
        text = str("_{0}".format(subject) + "_" + str(index))
        button = types.InlineKeyboardButton(text=teacher, callback_data=text)
        keyboard.add(button)
    bot.send_message(message.chat.id, "Выберите вашего учителя по предмету {0}:".format(subject), reply_markup=keyboard)


@bot.message_handler(commands=["start"])
def choose_class(message):
    if message.from_user.username in moderators:
        moderators[message.from_user.username] = message.chat.id
    if message.chat.id not in data:
        bot.send_message(message.chat.id, texts.start_message)
        data.update({message.chat.id: default})
        keyboard = types.InlineKeyboardMarkup()
        button_1 = types.InlineKeyboardButton(text="10", callback_data="10")
        button_2 = types.InlineKeyboardButton(text="11", callback_data="11")
        button_3 = types.InlineKeyboardButton(text="Другое", callback_data="12")
        keyboard.add(button_1, button_2, button_3)
        bot.send_message(message.chat.id, " А теперь предлагаю пройти регистрацию для более удобной работы с ботом.")
        bot.send_message(message.chat.id, "Выберите ваш класс:", reply_markup=keyboard)
    else:
        bot.send_message(message.chat.id, texts.start_message)


@bot.message_handler(commands=["changeclass"])
def change_class(message):
    if message.chat.id not in data:
        bot.send_message(message.chat.id, "Вы не прошли стартовую регистрацию!")
    else:
        keyboard = types.InlineKeyboardMarkup()
        button_1 = types.InlineKeyboardButton(text="10", callback_data="10")
        button_2 = types.InlineKeyboardButton(text="11", callback_data="11")
        button_3 = types.InlineKeyboardButton(text="Другое", callback_data="12")
        keyboard.add(button_1, button_2, button_3)
        bot.send_message(message.chat.id, "Выберите ваш класс:", reply_markup=keyboard)


@bot.message_handler(commands=["help"])
def help_message(message):
    bot.send_message(message.chat.id, texts.help_message)


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


@bot.message_handler(commands=["editclass"])
def change_info(message):
    if message.chat.id not in data or (not (data[message.chat.id].subjects["Базовая информатика"] != "" or\
            (data[message.chat.id].subjects["Программирование"] != "" and data[message.chat.id].subjects["Пользовательский курс"] and \
            data[message.chat.id].subjects["Теоретическая информатика"] != ""))):
        bot.send_message(message.chat.id, "Ошибка. Вы не прошли регистрацию или не являетесь лицеистом!")
    else:
        keyboard = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton(text="Профильный предмет", callback_data="edit_subject")
        button2 = types.InlineKeyboardButton(text="ФД", callback_data="edit_fd")
        button3 = types.InlineKeyboardButton(text="Вариативный предмет", callback_data="edit_variative")
        button4 = types.InlineKeyboardButton(text="Учителя", callback_data="edit_teacher")
        keyboard.add(button1, button2, button3, button4)
        bot.send_message(message.chat.id, "Что вы хотите изменить?", reply_markup=keyboard)


@bot.message_handler(commands=["give_mode"])
def give_mod(message):
    if message.from_user.username == misc.admin_nickname:
        moderators.update({message.text[11:]: 0})
    else:
        bot.send_message(message.chat.id, "У вас недостаточно прав!")


@bot.message_handler(commands=["unmode"])
def unmod(message):
    if message.from_user.username == misc.admin_nickname:
        try:
            moderators.pop(message.text[10:])
        except:
            bot.send_message(message.chat.id, "Произошла ошибка. Повторите попытку.")
    else:
        bot.send_message(message.chat.id, "У вас недостаточно прав!")


@bot.message_handler(commands=["announce"])
def change_ann(message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Да", callback_data="announce_yes"))
    keyboard.add(types.InlineKeyboardButton(text="Нет", callback_data="announce_no"))
    bot.send_message(message.chat.id, "Хотите ли вы получать рассылки?", reply_markup=keyboard)


@bot.message_handler(commands=["make_announce"])
def make_announce(message):
    if message.from_user.username not in moderators:
        for mod in moderators:
            if moderators[mod] != 0:
                bot.send_message(moderators[mod], message.text[15:])
        bot.send_message(message.chat.id, "Ваше объявление отправлено на рассмотрение модераторам.")
    else:
        for user in data:
            if data[user].announce == 1:
                bot.send_message(user, message.text[15:])


@bot.message_handler(commands=["timetable"])
def get_timetable(message):
    if message.chat.id not in data:
        bot.send_message(message.chat.id, text="Вы не прошли регистрацию!")
    elif data[message.chat.id].group == "12":
        another_timetable(message)
    else:
        keyboard = types.InlineKeyboardMarkup()
        button_1 = types.InlineKeyboardButton(text="На один день", callback_data="time_0")
        button_2 = types.InlineKeyboardButton(text="На всю неделю", callback_data="time_1")
        keyboard.add(button_1, button_2)
        bot.send_message(message.chat.id, text="Какое вы хотите расписание?", reply_markup=keyboard)


@bot.message_handler(commands=["add_teacher"])
def add_teacher(message):
    if message.from_user.username in moderators:
        text = re.split(r'&', message.text)
        try:
            teachers.subjects[text[1]].append(text[2])
            texts.teachers_texts.update({text[2]: text[3]})
            teachers.all_teachers.append(text[2])
            bot.send_message(message.chat.id, text="Изменения сохранены.")
        except:
            bot.send_message(message.chat.id, text="Неправильный формат данных.")
    else:
        bot.send_message(message.chat.id, text="У вас недостаточно прав!")


@bot.message_handler(commands=["delete_teacher"])
def add_teacher(message):
    if message.from_user.username in moderators:
        text = re.split(r'&', message.text)
        try:
            teachers.subjects[text[1]].pop(teachers.subjects[text[1]].index(text[2]))
            texts.teachers_texts.pop(text[2])
            teachers.all_teachers.pop(teachers.all_teachers.index(text[2]))
            bot.send_message(message.chat.id, text="Изменения сохранены.")
        except:
            bot.send_message(message.chat.id, text="Неправильный формат данных.")
    else:
        bot.send_message(message.chat.id, text="У вас недостаточно прав!")


@bot.message_handler(commands=["edit_description"])
def edit_description(message):
    if message.from_user.username in moderators:
        text = re.split(r'&', message.text)
        try:
            texts.teachers_texts[text[1]] = text[2]
            bot.send_message(message.chat.id, text="Изменения сохранены.")
        except:
            bot.send_message(message.chat.id, text="Неправильный формат данных.")
    else:
        bot.send_message(message.chat.id, text="У вас недостаточно прав!")


@bot.message_handler(commands=["add_lesson"])
def add_lesson(message):
    if message.from_user.username in moderators:
        text = re.split(r'&', message.text)
        try:
            with open('timetable.json', 'r') as t:
                  dat = json.load(t)
            dat[text[1]][text[2]][text[3]][text[4]].append({"subject": text[5], "teacher": text[6], "cabinet": text[7]})
            with open('timetable.json', 'w') as t:
                json.dump(dat, t)
            bot.send_message(message.chat.id, text="Изменения сохранены.")
        except:
            bot.send_message(message.chat.id, text="Неправильный формат данных.")
    else:
        bot.send_message(message.chat.id, text="У вас недостаточно прав!")


@bot.message_handler(commands=["delete_lesson"])
def add_lesson(message):
    if message.from_user.username in moderators:
        text = re.split(r'&', message.text)
        try:
            with open('timetable.json', 'r') as t:
                  dat = json.load(t)
            index = len(dat[text[1]][text[2]][text[3]][text[4]])
            now = 0
            for lesson in dat[text[1]][text[2]][text[3]][text[4]]:
                if lesson["subject"] == text[5] and lesson["teacher"] == text[6] and lesson["cabinet"] == text[7]:
                    index = now
                now += 1
            dat[text[1]][text[2]][text[3]][text[4]].pop(index)
            with open('timetable.json', 'w') as t:
                json.dump(dat, t)
            bot.send_message(message.chat.id, text="Изменения сохранены.")
        except:
            bot.send_message(message.chat.id, text="Неправильный формат данных.")
    else:
        bot.send_message(message.chat.id, text="У вас недостаточно прав!")


@bot.message_handler(commands=["edit_timetable"])
def edit_timetable(message):
    if message.from_user.username in moderators:
        text = re.split(r'&', message.text)
        try:
            with open('timetable.json', 'r') as t:
                  dat = json.load(t)
            index = len(dat[text[1]][text[2]][text[3]][text[4]])
            now = 0
            for lesson in dat[text[1]][text[2]][text[3]][text[4]]:
                if lesson["subject"] == text[5] and lesson["teacher"] == text[6] and lesson["cabinet"] == text[7]:
                    index = now
                now += 1
            if text[8] == "Предмет":
                dat[text[1]][text[2]][text[3]][text[4]][index]["subject"] = text[9]
            if text[8] == "Учитель":
                dat[text[1]][text[2]][text[3]][text[4]][index]["teacher"] = text[9]
            if text[8] == "Кабинет":
                dat[text[1]][text[2]][text[3]][text[4]][index]["cabinet"] = text[9]
            with open('timetable.json', 'w') as t:
                json.dump(dat, t)
            bot.send_message(message.chat.id, text="Изменения сохранены.")
        except:
            bot.send_message(message.chat.id, text="Неправильный формат данных.")
    else:
        bot.send_message(message.chat.id, text="У вас недостаточно прав!")


@bot.message_handler(commands=["edit_ivr_info"])
def edit_ivr_info(message):
    if message.from_user.username in moderators:
        text = re.split(r'edit_ivr_info ', message.text)
        texts.all_texts.pop(texts.all_texts.index(texts.ivr_info))
        texts.ivr_info = text[1]
        texts.all_texts.append(texts.ivr_info)
        bot.send_message(message.chat.id, "Изменения сохранены.")
    else:
        bot.send_message(message.chat.id, "У вас недостаточно прав!")


@bot.message_handler(commands=["edit_groups_info"])
def edit_groups_info(message):
    if message.from_user.username in moderators:
        text = re.split(r'edit_groups_info ', message.text)
        texts.all_texts.pop(texts.all_texts.index(texts.groups_info))
        texts.groups_info = text[1]
        texts.all_texts.append(texts.groups_info)
        bot.send_message(message.chat.id, "Изменения сохранены.")
    else:
        bot.send_message(message.chat.id, "У вас недостаточно прав!")


@bot.message_handler(commands=["edit_places_info"])
def edit_places_info(message):
    if message.from_user.username in moderators:
        text = re.split(r'edit_places_info ', message.text)
        texts.all_texts.pop(texts.all_texts.index(texts.places_info))
        texts.places_info = text[1]
        texts.all_texts.append(texts.places_info)
        bot.send_message(message.chat.id, "Изменения сохранены.")
    else:
        bot.send_message(message.chat.id, "У вас недостаточно прав!")


@bot.message_handler(commands=["edit_miem_info"])
def edit_miem_info(message):
    if message.from_user.username in moderators:
        text = re.split(r'edit_miem_info ', message.text)
        texts.all_texts.pop(texts.all_texts.index(texts.miem_info))
        texts.miem_info = text[1]
        texts.all_texts.append(texts.miem_info)
        bot.send_message(message.chat.id, "Изменения сохранены.")
    else:
        bot.send_message(message.chat.id, "У вас недостаточно прав!")


@bot.message_handler(commands=["edit_fkn_info"])
def edit_fkn_info(message):
    if message.from_user.username in moderators:
        text = re.split(r'edit_fkn_info ', message.text)
        texts.all_texts.pop(texts.all_texts.index(texts.fkn_info))
        texts.fkn_info = text[1]
        texts.all_texts.append(texts.fkn_info)
        bot.send_message(message.chat.id, "Изменения сохранены.")
    else:
        bot.send_message(message.chat.id, "У вас недостаточно прав!")


@bot.message_handler(commands=["edit_matfak_info"])
def edit_matfak_info(message):
    if message.from_user.username in moderators:
        text = re.split(r'edit_matfak_info ', message.text)
        texts.all_texts.pop(texts.all_texts.index(texts.matfak_info))
        texts.matfak_info = text[1]
        texts.all_texts.append(texts.matfak_info)
        bot.send_message(message.chat.id, "Изменения сохранены.")
    else:
        bot.send_message(message.chat.id, "У вас недостаточно прав!")


@bot.message_handler(commands=["edit_kompling_info"])
def edit_kompling_info(message):
    if message.from_user.username in moderators:
        text = re.split(r'edit_kompling_info ', message.text)
        texts.all_texts.pop(texts.all_texts.index(texts.kompling_info))
        texts.kompling_info = text[1]
        texts.all_texts.append(texts.kompling_info)
        bot.send_message(message.chat.id, "Изменения сохранены.")
    else:
        bot.send_message(message.chat.id, "У вас недостаточно прав!")


@bot.message_handler(commands=["edit_physfak_info"])
def edit_physfak_info(message):
    if message.from_user.username in moderators:
        text = re.split(r'edit_physfak_info ', message.text)
        texts.all_texts.pop(texts.all_texts.index(texts.physfak_info))
        texts.physfak_info = text[1]
        texts.all_texts.append(texts.physfak_info)
        bot.send_message(message.chat.id, "Изменения сохранены.")
    else:
        bot.send_message(message.chat.id, "У вас недостаточно прав!")


@bot.message_handler(commands=["edit_bi_info"])
def edit_groups_info(message):
    if message.from_user.username in moderators:
        text = re.split(r'edit_bi_info ', message.text)
        texts.all_texts.pop(texts.all_texts.index(texts.bi_info))
        texts.bi_info = text[1]
        texts.all_texts.append(texts.bi_info)
        bot.send_message(message.chat.id, "Изменения сохранены.")
    else:
        bot.send_message(message.chat.id, "У вас недостаточно прав!")


@bot.message_handler(content_types=['text'])
def answer_for_queries(message):
    text = re.split(r'\s', message.text)
    for word in range(len(text)):
        text[word] = text[word].lower()
    flag_whole = True
    for cur in texts.all_texts:
        now = re.split(r'[\s,.!?]', cur)
        for word in range(len(now)):
            now[word] = now[word].lower()
        for word in now:
            flag = True
            if word != "":
                for check in text:
                    if word in check:
                        flag = False
                        flag_whole = False
                        bot.send_message(message.chat.id, "Возможно вы искали:\n" + cur)
                        break
                if not flag:
                    break
    for cur in texts.teachers_texts:
        info = texts.teachers_texts[cur]
        now = re.split(r'[\s,.!?]', info)
        for word in range(len(now)):
            now[word] = now[word].lower()
        for word in now:
            flag = True
            if word != "":
                for check in text:
                    if word in check:
                        flag = False
                        flag_whole = False
                        bot.send_message(message.chat.id, "Возможно вы искали:\n" + info)
                        break
                if not flag:
                    break
    if flag_whole:
        bot.send_message(message.chat.id, "По вашему запросу ничего не найдено. Повторите запрос или воспользуйтесь командой /help")


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    # Расписание
    if call.data[:4] == "time":
        if data[call.message.chat.id].group == "10" or data[call.message.chat.id].group == "11":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            try:
                if call.data[-1] == "1":
                    with open('timetable.json', 'r') as t:
                        dat = json.load(t)
                        text = ""
                        for day in dat[data[call.message.chat.id].group][data[call.message.chat.id].kur_gr]:
                            if day == "Пятница":
                                text += "Четверг\n" + data[call.message.chat.id].fd + '\n\n'
                            text += day + "\n"
                            for num_of_lesson in dat[data[call.message.chat.id].group][data[call.message.chat.id].kur_gr][day]:
                                text += num_of_lesson + "\n"
                                flag = True
                                for possible in dat[data[call.message.chat.id].group][data[call.message.chat.id].kur_gr][day][num_of_lesson]:
                                    if possible["subject"] in teachers.var_subjects:
                                        if possible["subject"] == data[call.message.chat.id].dop_subj:
                                            flag = False
                                            text += "Предмет: {0}\nУчитель: {1}\nКабинет: {2}\n".format(
                                                possible["subject"], possible["teacher"], possible["cabinet"])
                                    elif data[call.message.chat.id].subjects[possible["subject"]] == possible["teacher"]:
                                        flag = False
                                        text += "Предмет: {0}\nУчитель: {1}\nКабинет: {2}\n".format(
                                                             possible["subject"], possible["teacher"], possible["cabinet"])
                                if flag:
                                    text += "Нет уроков\n"
                                text += "\n"
                        bot.send_message(call.message.chat.id, text=text)
                else:
                    one_day_timetable(call.message)
            except:
                bot.send_message(call.message.chat.id, text="Произошла ошибка.")

    if call.data[:5] == "other":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        if call.data[-1] == "0":
            bot.send_message(call.message.chat.id, text="По этой ссылке вы можете посмотреть учебный план: https://school.hse.ru/mirror/pubs/share/238309845")
        else:
            keyboard = types.InlineKeyboardMarkup()
            for group in range(10, 12):
                for num in range(1, 6):
                    if group != 10 or num != 5:
                        keyboard.add(types.InlineKeyboardButton(text="{0} класс {1} группа".format(str(group), str(num)), callback_data="class_{0}".format(str(group) + str(num))))
            bot.send_message(call.message.chat.id, text="Выберите группу:", reply_markup=keyboard)

    if call.data[:5] == "class":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        group = call.data[6:8]
        num = call.data[-1]
        try:
            with open('timetable.json', 'r') as t:
                dat = json.load(t)
                text = ""
                for day in dat[group][num]:
                    if day == "Пятница":
                        text += "Четверг\n" + "Факультетский день" + '\n\n'
                    text += day + "\n"
                    for num_of_lesson in dat[group][num][day]:
                        text += num_of_lesson + "\n"
                        for possible in dat[group][num][day][num_of_lesson]:
                            if possible["subject"] in teachers.var_subjects:
                                text += "Предмет: {0}\nУчитель: {1}\nКабинет: {2}\n".format(
                                    possible["subject"], possible["teacher"], possible["cabinet"])
                            else:
                                text += "Предмет: {0}\nУчитель: {1}\nКабинет: {2}\n".format(
                                        possible["subject"], possible["teacher"], possible["cabinet"])
                        text += "\n"
                bot.send_message(call.message.chat.id, text=text)
        except:
            bot.send_message(call.message.chat.id, text="Произошла ошибка.")

    if call.data[:3] == "day":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        day = call.data[4:]
        text = ""
        try:
            with open('timetable.json', 'r') as t:
                dat = json.load(t)
                for num_of_lesson in dat[data[call.message.chat.id].group][data[call.message.chat.id].kur_gr][day]:
                    text += num_of_lesson + "\n"
                    flag = True
                    for possible in dat[data[call.message.chat.id].group][data[call.message.chat.id].kur_gr][day][num_of_lesson]:
                        if possible["subject"] in teachers.var_subjects:
                            if possible["subject"] == data[call.message.chat.id].dop_subj:
                                flag = False
                                text += "Предмет: {0}\nУчитель: {1}\nКабинет: {2}\n".format(
                                    possible["subject"], possible["teacher"], possible["cabinet"])
                        elif data[call.message.chat.id].subjects[possible["subject"]] == possible["teacher"]:
                            flag = False
                            text += "Предмет: {0}\nУчитель: {1}\nКабинет: {2}\n".format(
                                possible["subject"], possible["teacher"], possible["cabinet"])
                    if flag:
                        text += "Нет уроков\n"
                    text += "\n"
            bot.send_message(call.message.chat.id, text=text)
        except:
            bot.send_message(call.message.chat.id, text="Произошла ошибка.")

    # Первая регистрация
    if call.data[0] == "1":
        data[call.message.chat.id].group = call.data
        bot.delete_message(call.message.chat.id, call.message.message_id)
        if call.data == "10" or call.data == "11":
            choose_group(call.message)
        else:
            data[call.message.chat.id].subjects["Пользовательский курс"] = ""
            data[call.message.chat.id].subjects["Программирование"] = ""
            data[call.message.chat.id].subjects["Базовая информатика"] = ""
            data[call.message.chat.id].subjects["Теоретическая информатика"] =""
            data[call.message.chat.id].group = call.data

    if call.data[:4] == "type":
        data[call.message.chat.id].kur_gr = call.data[4:]
        bot.delete_message(call.message.chat.id, call.message.message_id)
        choose_profile_subject(call.message)

    if call.data == "physics_prof" or call.data == "inf_prof":
        data[call.message.chat.id].specialization = call.data
        bot.delete_message(call.message.chat.id, call.message.message_id)
        choose_var(call.message)

    if call.data[:3] == "var":
        data[call.message.chat.id].dop_subj = call.data[4:]
        bot.delete_message(call.message.chat.id, call.message.message_id)
        choose_fd(call.message)

    if call.data[:2] == "ch":
        data[call.message.chat.id].fd = call.data[3:]
        bot.delete_message(call.message.chat.id, call.message.message_id)
        choose_teachers(call.message, 0)

    if call.data[:7] == "teacher":
        data[call.message.chat.id].subjects[teachers.subjects_names[data[call.message.chat.id].cnt_for_reg - 1]] \
            = call.data[8:]
        bot.delete_message(call.message.chat.id, call.message.message_id)
        if data[call.message.chat.id].cnt_for_reg > 7:
            data[call.message.chat.id].cnt_for_reg = 1
            if data[call.message.chat.id].specialization == "physics_prof":
                choose_one_subject(call.message, "Базовая информатика")
            else:
                choose_one_subject(call.message, "Теоретическая информатика")
                choose_one_subject(call.message, "Программирование")
                choose_one_subject(call.message, "Пользовательский курс")
        else:
            choose_teachers(call.message, data[call.message.chat.id].cnt_for_reg)
            data[call.message.chat.id].cnt_for_reg += 1

    # ФД
    if call.data == "bi":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, texts.bi_info)

    if call.data == "phys_fak":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, texts.physfak_info)

    if call.data == "math":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, texts.matfak_info)

    if call.data == "fkn":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, texts.fkn_info)

    if call.data == "kompling":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, texts.kompling_info)

    if call.data == "miem":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, texts.miem_info)

    # Учителя
    if call.data in teachers.subjects:
        bot.delete_message(call.message.chat.id, call.message.message_id)
        keyboard = types.InlineKeyboardMarkup()
        for teacher in teachers.subjects[call.data]:
            keyboard.add(types.InlineKeyboardButton(text=teacher, callback_data=teacher))
        bot.send_message(call.message.chat.id, "Выберите учителя:", reply_markup=keyboard)

    if call.data in teachers.all_teachers:
        bot.delete_message(call.message.chat.id, call.message.message_id)
        if texts.teachers_texts[call.data] != "":
            bot.send_message(call.message.chat.id, texts.teachers_texts[call.data])
        else:
            bot.send_message(call.message.chat.id, "К сожалению, про этого учителя еще нет информации.")

    # Редактирование информации
    if call.data[0] == "_":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        now = re.split(r'_', call.data)
        data[call.message.chat.id].subjects[now[1]] = teachers.subjects[now[1]][int(now[2])]
        bot.send_message(call.message.chat.id, "Изменения сохранены.")

    if call.data[:3] == "sub":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        choose_one_subject(call.message, call.data[4:])

    if call.data == "edit_teacher":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        keyboard = types.InlineKeyboardMarkup()
        for subject in teachers.subjects:
            keyboard.add(types.InlineKeyboardButton(text=subject, callback_data="sub_{0}".format(subject)))
        bot.send_message(call.message.chat.id, "По какому предмету вы хотите изменить учителя?", reply_markup=keyboard)

    if call.data == "edit_variative":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        edit_var(call.message)

    if call.data[:4] == "evar":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        data[call.message.chat.id].dop_subj = call.data[5:]
        bot.send_message(call.message.chat.id, "Изменения сохранены.")

    if call.data == "edit_subject":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        edit_profile_subject(call.message)

    if call.data[:5] == "e_sub":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        data[call.message.chat.id].specialization = call.data[6:]
        if call.data[6:] == "physics_prof":
            data[call.message.chat.id].subjects["Теоретическая информатика"] = ""
            data[call.message.chat.id].subjects["Программирование"] = ""
            data[call.message.chat.id].subjects["Пользовательский курс"] = ""
            choose_one_subject(call.message, "Базовая информатика")
        else:
            data[call.message.chat.id].subjects["Базовая информатика"] = ""
            choose_one_subject(call.message, "Теоретическая информатика")
            choose_one_subject(call.message, "Программирование")
            choose_one_subject(call.message, "Пользовательский курс")

    if call.data == "edit_fd":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        edit_fd(call.message)

    if call.data[:4] == "e_fd":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        data[call.message.chat.id].specialization = call.data[5:]
        bot.send_message(call.message.chat.id, "Изменения сохранены.")

    # Рассылки
    if call.data[:8] == "announce":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        if call.message.chat.id not in data:
            bot.send_message(call.message.chat.id, "Вы не прошли решистрацию!")
        else:
            if call.data[9:] == "yes":
                data[call.message.chat.id].announce = 1
            else:
                data[call.message.chat.id].announce = 0
            bot.send_message(call.message.chat.id, "Изменения сохранены.")


if __name__ == '__main__':
    bot.polling(none_stop=True)
