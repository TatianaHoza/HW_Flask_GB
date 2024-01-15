from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Email, Length


class Registration(FlaskForm):
    username = StringField('Имя', validators=[DataRequired()])
    user_surname = StringField('Фамилия', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль',validators=[DataRequired(),Length(min=4)])
    submit = SubmitField('Зарегистрировать')


