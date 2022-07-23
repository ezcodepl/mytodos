from flask import Flask, render_template, request, redirect
from flask_bootstrap import Bootstrap5
import athlete_dao
import todo_dao
from todo_dao import Todos

app = Flask(__name__)
bootstrap = Bootstrap5(app)

@app.route('/')
def index():  # put application's code here
    return render_template('index.html', data=todo_dao.get_all_front())


@app.route('/todos')
def todos():  # put application's code here
    return render_template('todos.html', data=todo_dao.get_all())


@app.route('/todos_details')
def todos_details():  # put application's code here
    id = request.args.get('id')
    #print(f'Szczegóły zadania o id={id}')
    a = todo_dao.get_one(id)

    if a.priority == 1:
        card = 'card text-white bg-danger mb-3'
    elif a.priority ==2:
        card = 'card text-white bg-warning mb-3'
    else:
        card = 'card text-white bg-success mb-3'

    return render_template('todos_details.html', id=id, details=a, data=todo_dao, card=card)

@app.route('/add_todo')
def add_todo():  # put application's code here
    return render_template('add_todo.html')

@app.route('/add_todo', methods=['POST'])
def add_todo_post():  # put application's code here
    title=request.form['title']
    description = request.form['description']
    priority = request.form['priority']
    todo = Todos(None, title, description, priority)
    todo_dao.save_todo(todo)
    return redirect('/todos')

@app.route('/edit_todo')
def edit_todo():  # put application's code here
    id = request.args.get('id')
    #print(f'Szczegóły zadania o id={id}')
    e = todo_dao.get_one(id)
    return render_template('edit_todo.html', edit = e)

@app.route('/edit_todo', methods=['POST'])
def edit_todo_post():  # put application's code here
    title = request.form['title']
    description = request.form['description']
    priority = request.form['priority']
    id = request.args.get('id')
    todo = Todos(None, title, description, priority)
    todo_dao.update_todo(todo,id)
    return redirect('/todos')

@app.route('/del_todo')
def del_todo():  # put application's code here
    id = request.args.get('id')
    #print(f'Szczegóły zadania o id={id}')
    todo_dao.del_todo(id)
    return redirect('/todos')

@app.route('/about')
def about():  # put application's code here
    lista = ['python', 'html', 'flask']
    return render_template('about.html', imie='Ernest', nazwisko='Zając', email='ernest.zajac@gmail.com', lista=lista)


@app.route('/examples')
def examples():  # put application's code here
    result = athlete_dao.get_all()
    # for e in result:
    #     print(e)
    return render_template('examples.html', some_number=12345, data=result)

if __name__ == '__main__':
    app.run(debug=True, port=80)
