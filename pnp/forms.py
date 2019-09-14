from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, DateField, TextAreaField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from pnp.models import User
from flask_login import current_user


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


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=120)])
    confirm_email = StringField('Email', validators=[DataRequired(), Email()])

    first_name = StringField('First Name', validators=[DataRequired(), Length(min=2, max=30)])
    second_name = StringField('Second Name', validators=[DataRequired(), Length(min=2, max=40)])
    birth_date = DateField('Birth date', validators=[DataRequired()])
    picture = FileField('Update profile picture', validators=[FileAllowed(['jpg', 'png'])])

    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('Username already taken. Please choose a different one.')

    def validate_email(self, email):
        if email.data != current_user.email:
            email = Email.query.filter_by(email=email.data).first()
            if email:
                raise ValidationError('Email already in use.')


class GameForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    submit = SubmitField('Create')


class CharacterForm(FlaskForm):
    first_name = StringField('Surname', validators=[DataRequired(), Length(min=2, max=30)])
    second_name = StringField('Name', validators=[DataRequired(), Length(min=2, max=40)])
    race = StringField('Race', validators=[DataRequired(), Length(min=2, max=50)])
    role = StringField('Class', validators=[DataRequired(), Length(min=2, max=50)])
    gender = IntegerField('Gender', validators=[DataRequired(), Length(min=2, max=30)])
    age = StringField('Age', validators=[DataRequired()])
    weight = StringField('Weight', validators=[DataRequired(), Length(min=2, max=30)])
    height = StringField('Height', validators=[DataRequired(), Length(min=2, max=30)])
    hair = StringField('Hair', validators=[DataRequired(), Length(min=2, max=50)])
    body = StringField('Body', validators=[DataRequired(), Length(min=2, max=30)])

    submit = SubmitField('Update')