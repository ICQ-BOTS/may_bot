import sqlite3
import random

database = 'database.sqlite'

def init_db():
    connect = sqlite3.connect(database)
    cursor = connect.cursor()
    cursor.execute("""
    CREATE table pictures (
        id integer primary key,
        author text,
        name text,
        surname text,
        rank text,
        photo text,
        photo_result text,
        status text
    );
    """)
    connect.close()

def get_picture(post_id=None):
    connect = sqlite3.connect(database)
    cursor = connect.cursor()
    if post_id == None:
        cursor.execute("SELECT * FROM pictures WHERE photo_result='none'")
    else:
        cursor.execute("SELECT * FROM pictures WHERE id="+str(post_id))
    pictures = cursor.fetchall()
    connect.close()
    if pictures:
        picture = list(pictures[0])
    else:
        return []
    return picture

def add_new(author,name,surname,rank,photo):
    connect = sqlite3.connect(database)
    cursor = connect.cursor()
    cursor.execute("SELECT id FROM pictures")
    try:
        new_id = str(cursor.fetchall()[-1][0] + 1)
    except:
        new_id = 1
    cursor.execute("insert into pictures values ("+str(new_id)+",'"+author+"','"+name+"','"+surname+"','"+rank+"','"+photo+"','none','no_posted')")
    connect.commit()
    connect.close()
    return new_id
    
def update_status(id_post):
    connect = sqlite3.connect(database)
    cursor = connect.cursor()
    cursor.execute("UPDATE pictures SET status='posted' where id="+str(id_post))
    connect.commit()
    connect.close()

def update_photo_result(id_post,photo_result):
    connect = sqlite3.connect(database)
    cursor = connect.cursor()
    cursor.execute("UPDATE pictures SET photo_result='"+photo_result+"' where id="+str(id_post))
    connect.commit()
    connect.close()

def get_db(table):
    connect = sqlite3.connect(database)
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM "+table)
    result = cursor.fetchall()
    connect.close()
    return result

if __name__ == '__main__': 
	init_db()
    # print(get_db("pictures"))
