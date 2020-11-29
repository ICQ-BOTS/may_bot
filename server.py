# -*- coding: utf8 -*-

import database
import config
import json

def message_processing(bot, event):#bot, event
    data = event.data
    if data["chat"]["type"] == "private":
        try:
            photo = data['parts'][0]["payload"]["fileId"]
        except:
            photo = ""
        if photo:
            try:
                text = data.get('parts')[0].get('payload').get('caption')
                if text.strip():
                    add_new(bot,data,text,photo)
                else:
                    message = """Фото отправлено без текста. Ознакомьтесь, пожалуйста, с инструкцией выше\n\nУ вас должно получиться вот так:"""
                    bot.send_text(chat_id=data["chat"]["chatId"], text=message)
                    caption = """Савин Федор стaрший сержант"""
                    photo = "08Ide000j2SWYbxv2zLTog5eb4957e1bd"
                    bot.send_file(chat_id=data["chat"]["chatId"], caption=caption, file_id=photo)
            except:
                message = """Фото отправлено без текста. Ознакомьтесь, пожалуйста, с инструкцией выше\n\nУ вас должно получиться вот так:"""
                bot.send_text(chat_id=data["chat"]["chatId"], text=message)
                caption = """Савин Федор стaрший сержант"""
                photo = "08Ide000j2SWYbxv2zLTog5eb4957e1bd"
                bot.send_file(chat_id=data["chat"]["chatId"], caption=caption, file_id=photo)
        else:
            main_message(bot,data)

def main_message(bot,data):
    message = """С помощью этого бота вы можете обработать фотографию вашего ветерана и отправить ее в виртуальное Шествие Бессмертного полка прямо в ICQ New - https://icq.im/ourheroes"""
    bot.send_text(chat_id=data["chat"]["chatId"], text=message)
    message = """Пожалуйста, загрузите фотографию вашего ветерана и сразу же при выборе фотографии укажите его Фамилию, Имя и звание.\nЗатем вы можете скачать полученную фотографию и отправить ее в Бессмертный полк.\n\nЕсли у вас возникли сложности, ознакомьтесь с видео инструкцией."""
    bot.send_text(chat_id=data["chat"]["chatId"], text=message)
    video = "876fu000YLIgP56Tlf9uvN5eb572841ae"
    bot.send_file(chat_id=data["chat"]["chatId"], file_id=video)


def add_new(bot,data,text,photo):
    rank = ""
    text_arr = text.split(" ")
    for i in range(2,len(text_arr)):
        rank += text_arr[i] + " "
    database.add_new(data["chat"]["chatId"],text_arr[0],text_arr[1],rank,photo)
    text = "Фотография создается, подождите немного"
    bot.send_text(chat_id=data["chat"]["chatId"], text=text)

def button_processing(bot, event):
    data = event.data
    if data["message"]["chat"]["type"] == "private":
        func_arr = data["callbackData"].split("_")
        picture = database.get_picture(func_arr[1])
        inlineKeyboardMarkup = json.dumps([
            [{"text": "Опубликовать", "callbackData": "func_post_"+str(picture[0])+"_"+str(picture[1])}],
            [{"text": "Не публиковать", "callbackData": "func_delete_"+str(picture[0])+"_"+str(picture[1])}]
        ])
        bot.send_file(chat_id=config.admin_channel, file_id=picture[6], inline_keyboard_markup=inlineKeyboardMarkup)
        text = "Фотография успешно предложена и отправлена на модерацию"
        bot.send_text(chat_id=data["message"]["chat"]["chatId"], text=text)
    else:
        if data["message"]["chat"]["chatId"] == "682722533@chat.agent":
            if "func_post" in data["callbackData"]:
                id_post = data["callbackData"][10:]
                post_process(bot,id_post,data,"post")
            elif "func_delete" in data["callbackData"]:
                text = data["callbackData"][12:]
                post_process(bot,text,data,"delete")


def post_process(bot,text,data,proc_type):
    id_post = text[0]
    picture = database.get_picture(id_post)
    print(picture)
    if picture[7]=="no_posted":
        if proc_type == "delete":
            admin_text = "Пост успешно удален"
            bot.send_text(chat_id=config.admin_channel, text=admin_text)
            return
        text = picture[1]
        admin_text = "Пост успешно опубликован"
        bot.send_file(chat_id=config.channel, file_id=picture[6])
    else:
        admin_text = "Данный пост уже обработан"
    bot.send_text(chat_id=config.admin_channel, text=admin_text)
    database.update_status(id_post)
