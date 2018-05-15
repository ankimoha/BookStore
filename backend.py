import sqlite3

def connect():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY,title text,author text,year integer,isbn integer)")
    conn.commit()
    conn.close()

def insert(title,author,year,isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(title,author,year,isbn))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    conn.close()
    return rows

def search(title="",author="",year="",isbn=""):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book where title = ? OR author = ? OR year = ? OR isbn = ?", (title,author,year,isbn))
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM book where id = ?",(id,))
    conn.commit()
    conn.close()

def update(id,title,author,year,isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("UPDATE book set title = ?, author = ?,year = ?,isbn = ? where id = ?",(title,author,year,isbn,id))
    conn.commit()
    conn.close()

connect()
'''insert commands'''
# insert("Fountainhead","Ayn Rand",1936,987456321)
# insert("The Shining","Stephen King",1978,98563214)
# insert("Little Fires Everywhere","Celeste Ng",2017,1254125)
'''delete command'''
# delete(5)
'''update command'''
# update(4,"The Shining","Stanley Kubrick",1985,9658965)
'''print all the values '''
print(view())
''''search the records'''
# print(search(author= "Ayn Rand"))
