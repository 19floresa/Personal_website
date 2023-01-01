from flask import render_template, flash, redirect, url_for, request
# return render_template("<file_name.html>", "<title="<something>">", ...)
# Note: title can be any variable you defined in the html file
from werkzeug.urls import url_parse
from app import app, db
from app.forms import LoginForm, RegistrationForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User

@app.route('/')
@app.route('/index')
@login_required
def index():
    posts = [
            {
            
                'author':{'username': 'John'},
                'body':'Beautiful day in Vancouver!'
                
            },
            {
            
                'author':{'username': 'Smith'},
                'body':'Good day!'
                
            }
            ]
    
    # render the index web page
    return render_template('index.html', title='Home Page', posts=posts)


@app.route("/login", methods=['GET', 'POST'])
def login():
    # check if user is already logged in
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    # login class created in  a differed file
    form = LoginForm()
    
    if form.validate_on_submit():
        # look for the user
        user = User.query.filter_by(username=form.username.data).first()
        
        # flash error if no user or incorrect password
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        
        # registed the user as logged in for that user
        login_user(user, remember=form.remember_me.data)

        # redirect back if succesful login
        next_page = request.args.get('next')
        # no next arg or domain outside website then redirect to index
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')

        # user logged in
        return redirect(next_page)

    # render the login webpage
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))

    return render_template('register.html', title='Register', form=form)

