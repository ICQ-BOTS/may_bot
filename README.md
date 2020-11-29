
# May9Bot

Старт:
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