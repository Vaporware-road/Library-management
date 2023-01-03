# written by Abyss
# python 3.11.1

import sqlite3


# back-end part of project library management
# this part contain the back-end of my project 

def connect():
    conn = sqlite3.connect(r"./books.db")
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS books (id INTIGER PRIMARY KEY, title text,athur text,year INTIGER, ISBN INTIGER)")
    conn.commit()
    conn.close()


def insert(title, athur, year, ISBN):
    conn = sqlite3.connect(r"./books.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO books VALUES (NULL,?,?,?,?)", (title, athur, year, ISBN))
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows


def view():
    conn = sqlite3.connect(r"./books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM books")
    conn.commit()
    conn.close()


insert("python OOP", "Dusty philips", 2015, 1130815)
print(view())

connect()
