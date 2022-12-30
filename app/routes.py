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
    
    # render the index web page
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route("/login", methods=['GET', 'POST'])
def login():
    # login class created in  a differed file
    form = LoginForm()
    
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        # user logged in
        return redirect(url_for('index'))

    # render the login webpage
    return render_template('login.html', title='Sign In', form=form)



