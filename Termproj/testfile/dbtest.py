import sqlite3

conn = sqlite3.connect('blog.db')
c = conn.cursor()  # 커서 생성
c.execute('''CREATE TABLE blog (id integer PRIMARY KEY, subject text, content text, date text)''')