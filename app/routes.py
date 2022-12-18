from flask import render_template
# return render_template("<file_name.html>", "<title="<something>">", ...)
#Note: title can be any variable you defined in the html file
from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"
