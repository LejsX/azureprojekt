from flask import Flask, render_template, request, redirect, url_for
from models import db, Task
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.route('/')
def index():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        new_task = Task(title=title, description=description)
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_task.html')

@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)
    if request.method == 'POST':  # Usunięty zbędny nawias
        task.title = request.form['title']
        task.description = request.form['description']
        task.status = request.form['status']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit_task.html', task=task)

if __name__ == '__main__':
    app.run(debug=True)
