
# May9Bot

# Оглавление 
 - [Описание](https://github.com/ICQ-BOTS/may_bot#описание)
 - [Установка](https://github.com/ICQ-BOTS/may_bot#установка)
 - [Скриншоты работы](https://github.com/ICQ-BOTS/may_bot#скриншоты-работы)

# Описание
С помощью этого бота вы можете обработать фотографию вашего ветерана и отправить ее в виртуальное Шествие Бессмертного полка прямо в ICQ New.

# Установка

1. Установка всех зависимостей 
```bash
pip3 install -r requirements.txt
```

2. Инициализация базы данных
```bash
python3 database.py
```

3. Вставляем данные в config.py
* Токен
* Ид админской группы
* Ид канала для публикации постов

4. Запуск процесса rendering!
```bash
python3 rendering.py &
```
 
5. Запуск бота!
```bash
python3 may_bot.py
```

# Скриншоты работы
<img src="https://github.com/ICQ-BOTS/may_bot/blob/main/img/1.png" width="400">
<img src="https://github.com/ICQ-BOTS/may_bot/blob/main/img/2.png" width="400">
<img src="https://github.com/ICQ-BOTS/may_bot/blob/main/img/result.jpg" width="400">