from flask import Flask, render_template, redirect, url_for, flash, request, session
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

# Dummy user data
users = {'gomolemontlhane@gmail.com': 'password123'}

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(min=6, max=35)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=20)])
    submit = SubmitField('Login')

class SignupForm(FlaskForm):
    firstname = StringField('Firstname', validators=[DataRequired(), Length(min=2, max=30)])
    email = StringField('Email', validators=[DataRequired(), Length(min=6, max=35)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=20)])
    repeat_password = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Signup')

@app.route('/')
def home():
    if 'username' in session:
        return redirect(url_for('success'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        if email in users and users[email] == password:
            session['username'] = email
            flash('Login successful!', 'success')
            return redirect(url_for('success'))
        else:
            flash('Invalid email or password', 'danger')

    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        firstname = form.firstname.data
        email = form.email.data
        password = form.password.data

        flash('Signup successful! Please log in.')
        return redirect(url_for('login'))
    
    return render_template('signup.html', form=form)

@app.route('/success')
def success():
    if 'username' not in session:
        flash('You need to log in first!', 'warning')
        return redirect(url_for('login'))

    return render_template('success.html')

if __name__ == "__main__":
    app.run(debug=True)
