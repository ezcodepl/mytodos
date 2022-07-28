import psycopg2
import mysql.connector
from domain import Todos

def get_all_msql():
    result= []
    connection = mysql.connector.connect(host='localhost', port=3306, database='test', user='root', password='')
    cursor = connection.cursor()
    cursor.execute('select * from todos order by todo_id asc')
    res = cursor.fetchall()
    for w in res:
        a = Todos(w[0], w[1], w[2], w[3], w[4], w[5], w[6])
        result.append(a)
    connection.close()
    return result

def get_all_fake():
    result = []
    result.append(Todos(1, 'zadanie 1', 'treść zadania 1', 1))
    result.append(Todos(2, 'zadanie 2', 'treść zadania 2', 2))
    result.append(Todos(3, 'zadanie 3', 'treść zadania 3', 3))
    return result

def get_all():
    result= []
    connection = mysql.connector.connect(host='localhost', port=3306, database='test', user='root', password='')
    cursor = connection.cursor()
    cursor.execute('select * from todos order by todo_id asc')
    for w in cursor:
        a = Todos(w[0], w[1], w[2], w[3], w[4], w[5], w[6])
        result.append(a)
    connection.close()
    return result

def get_one(id):
    connection = mysql.connector.connect(host='localhost', port=3306, database='test', user='root', password='')
    cursor = connection.cursor()
    cursor.execute(f"select * from todos where todo_id={id}")
    w = cursor.fetchone()
    print(w)
    a = Todos(w[0], w[1], w[2], w[3], w[4], w[5], w[6])
    connection.close()
    return a

def save_todo(todo):
    sql = f"insert into todos(todo_title,todo_description,priority) values('{todo.todo_title}','{todo.todo_description}',{todo.priority})"
    connection = mysql.connector.connect(host='localhost', port=3306, database='test', user='root', password='')
    cursor = connection.cursor()
    cursor.execute(sql)
    connection.commit()

def update_todo(todo,id):
    sql = f"update todos set todo_title='{todo.todo_title}' ,todo_description='{todo.todo_description}', priority = '{todo.priority}' where todo_id='{id}' "
    connection = mysql.connector.connect(host='localhost', port=3306, database='test', user='root', password='')
    cursor = connection.cursor()
    cursor.execute(sql)
    connection.commit()

def del_todo(id):
    sql = f"delete from todos where todo_id={id}"
    connection = mysql.connector.connect(host='localhost', port=3306, database='test', user='root', password='')
    cursor = connection.cursor()
    cursor.execute(sql)
    connection.commit()

def get_all_front():
    result= []
    connection = mysql.connector.connect(host='localhost', port=3306, database='test', user='root', password='')
    cursor = connection.cursor()
    cursor.execute('select * from todos order by priority asc')
    for w in cursor:
        a = Todos(w[0], w[1], w[2], w[3], w[4], w[5], w[6])
        result.append(a)
    connection.close()
    return result