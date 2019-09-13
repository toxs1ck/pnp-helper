from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from pnp.models import User


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=120)])
    confirm_email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])

    first_name = StringField('First Name', validators=[DataRequired(), Length(min=2, max=30)])
    second_name = StringField('Second Name', validators=[DataRequired(), Length(min=2, max=40)])
    birth_date = DateField('Birth date', validators=[DataRequired()])

    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already taken. Please choose a different one.')

    def validate_email(self, email):
        email = Email.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError('Email already in use.')

    def validate_password(self, password, password_validation):
        user = User.query.filter_by(usernem=username.data).first()
        if user:
            raise ValidationError('Validation Massage')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
