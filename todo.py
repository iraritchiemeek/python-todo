import sqlite3
from bottle import route, run

@route('/doesthiswork')
@route('/todo')
def todo_list():
    con = sqlite3.connect('todo.db')
    c = con.cursor()
    c.execute("SELECT id, task FROM todo WHERE status LIKE '1'")
    result = c.fetchall()
    return str(result)

run()