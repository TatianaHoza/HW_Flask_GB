'''Задание №8
Создать форму для регистрации пользователей на сайте.
Форма должна содержать поля "Имя", "Фамилия", "Email",
"Пароль" и кнопку "Зарегистрироваться".
При отправке формы данные должны сохраняться в базе
данных, а пароль должен быть зашифрован.
'''

from flask import Flask,render_template,request, redirect, url_for
from hashlib import sha256
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from HW_3.forms import Registration
from HW_3.model import User,db

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
csrf = CSRFProtect(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.db'
db.init_app(app)

@app.cli.command('create-db')
def create_db():
    db.create_all()

@app.route('/', methods = ['GET','POST'])
def index():
    form = Registration()
    if form.validate_on_submit():
        user = User(username = form.username.data, user_surname = form.user_surname.data, email = form.email.data,
                    password = sha256(form.password.data.encode(encodings = 'utf-8')).hexdigest())
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
