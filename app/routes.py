from flask import render_template, flash, redirect, url_for
# return render_template("<file_name.html>", "<title="<something>">", ...)
#Note: title can be any variable you defined in the html file
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {"username": "Alex"}
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
    
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))

    return render_template('login.html', title='Sign In', form=form)



