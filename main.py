from flask import Flask, render_template, request, url_for, redirect
# flash, send_from_directory
# from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
# from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user


app = Flask(__name__)
#
#
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# #CREATE TABLE IN DB
# class User(UserMixin, db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(100), unique=True)
#     password = db.Column(db.String(100))
#     name = db.Column(db.String(1000))
#
#     def check_password(self, password):
#         pass


# Line below only required once, when creating DB.
# db.create_all()
#
# login_manager = LoginManager()
# login_manager.init_app(app)

# create the todo_list database
class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(250), nullable=False)


# db.create_all()


# Home page - List all tasks with edit, add and delete functionality
@app.route('/')
def home():
    all_tasks = db.session.query(Tasks).all()
    return render_template('index.html', list_tasks=all_tasks)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == 'POST':
        task = request.form.get('task')
        new_task = Tasks(task=f"{task}")
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html')


@app.route('/edit', methods=['GET', 'POST'])
def edit():
    task_id = request.args.get('id')
    print(task_id)
    task_selected = Tasks.query.get(task_id)
    if request.method == 'POST':
        task_id = request.form['id']
        new_task = request.form.get('task')
        task_to_update = Tasks.query.get(task_id)
        task_to_update.task = new_task
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('edit.html', task=task_selected)


@app.route('/delete', methods=['GET', 'POST'])
def delete_task():
    task_id = request.args.get('id')
    task_to_delete = Tasks.query.get(task_id)
    db.session.delete(task_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
