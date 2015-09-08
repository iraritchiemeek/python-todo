import sqlite3
con = sqlite3.connect('todo.db')
con.execute("CREATE TABLE todo (id INTEGER PRIMARY KEY, task char(100) NOT NULL, status bool NOT NULL)")
con.execute("INSERT INTO todo (task,status) VALUES ('Learn Python',0)")
con.execute("INSERT INTO todo (task,status) VALUES ('Learn other stuff',0)")
con.execute("INSERT INTO todo (task,status) VALUES ('Learn more other sruff',0)")
con.execute("INSERT INTO todo (task,status) VALUES ('Learn more more other stuff',1)")
con.commit()