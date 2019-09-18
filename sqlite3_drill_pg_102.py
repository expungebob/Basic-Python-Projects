import sqlite3

connection = sqlite3.connect("textfiles.db")

cursor = connection.cursor()
with connection:
    cursor.execute("CREATE TABLE IF NOT EXISTS files (ID INTEGER PRIMARY KEY AUTOINCREMENT,file_name TEXT)")
    connection.commit()
connection.close()


connection = sqlite3.connect("textfiles.db")
cursor= connection.cursor()

fileList = ('information.docx', 'Hello.txt', 'myImage.png', 'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

insert = 'INSERT INTO files (file_name) VALUES (?)'

for file in fileList:
    if file.endswith(".txt"):
        cursor.execute(insert,[file])
        connection.commit()

cursor.execute("SELECT file_name FROM files")

result = cursor.fetchall()

for value in result:
    msg = "File Name: {}".format(value[0])
    print(msg)













