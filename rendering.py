import json
import time
from io import BytesIO

import requests
from bot.bot import Bot
from PIL import Image, ImageDraw, ImageFont

import config
import database

font_name = ImageFont.truetype('fonts/TT Norms Pro Bold.ttf',47)
text_color_name = (0,0,0)
font_rank = ImageFont.truetype('fonts/TT Norms Pro Regular.ttf',33)
text_color_rank = (53,205,29)

def render(bot,picture):
    buffered = BytesIO()
    try:
        background = Image.open('img/photo.png')
    except:
        database.update_photo_result(picture[0],"Картинка поломана")
    url = bot.get_file_info(file_id = picture[5]).json()["url"]
    resource = requests.get(url)
    out = open("img/photo.png", "wb")
    out.write(resource.content)
    out.close()

    img = Image.open('img/frame.png')
    photo = Image.open('img/photo.png')
    width, height = photo.size
    if width < height:
        coef_photo = width/500
        resized_photo = photo.resize((500,int(height/coef_photo)))
        img.paste(resized_photo, (150, 140))
    else:
        coef_photo = height/580
        resized_photo = photo.resize((int(width/coef_photo),580))
        img.paste(resized_photo, ((800 - int(width/coef_photo)) // 2, 140))
    
    frame = Image.open('img/frame.png')
    img.paste(frame, (0, 0),frame)

    draw = ImageDraw.Draw(img)
    text_name = picture[2] + " " + picture[3]
    text_rank = picture [4]
    text_width_name, text_height_name = draw.textsize(text_name, font_name)
    text_width_rank, text_height_rank = draw.textsize(text_rank.upper(), font_rank)
    draw.text(((800 - text_width_name) // 2, 840), text_name, text_color_name, font_name)
    draw.text(((800 - text_width_rank) // 2, 930), text_rank.upper(), text_color_rank, font_rank)

    img = img.convert("RGB")
    img.save('img/result.png')

    inlineKeyboardMarkup = json.dumps([
        [{"text": "➡️Отправить в Бессмертный полк", "callbackData": "post_"+str(picture[0]),"style": "primary"}]
    ])
    with open("img/result.png", "rb") as result_file:
        try: 
            img_result = bot.send_file(chat_id=picture[1], file=result_file, inline_keyboard_markup=inlineKeyboardMarkup).json()
        except:
            database.update_photo_result(picture[0],"Картинка поломана")
            return
    message = """Большое спасибо за участие в акции! Поделитесь этой фотографией со своими друзьями и в социальных сетях. Пусть в нашем полку окажется как можно больше героев!\n\nНажав на кнопку, вы соглашаетесь с публикацией вашей фотографии в канале «Шествие Бессмертного полка»"""
    bot.send_text(chat_id=picture[1], text=message)
    print(img_result)
    database.update_photo_result(picture[0],img_result["fileId"])

if __name__ == '__main__':
    bot = Bot(token=config.TOKEN)
    while True:
        try:
            picture = database.get_picture()
            if picture:
                render(bot, picture)
        except:
            time.sleep(2)

