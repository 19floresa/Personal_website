# Personal_website
source venv/bin/activate
Run:

In the command line type....
    export FLASK_APP=Personal_website.py
    flask run

_________________________________________________________

Assumption: when __init__.py was called it imported models, which had
the class User (a database), and put it into the context of my program.

cmds to call:
    
    - flask db init
        * managet for database

    -flask db migrate -m "users table"
        * creates the database in the context; [calls it users table]?

    - flask db upgrade
        * show the changes

    - flask dv downgrade
        * goes to the previous changes
