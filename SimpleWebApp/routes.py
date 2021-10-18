# as it's not a best practise to keep all the code in one file, we create a separate file for routes
# then, we will keep the routes here, and all the content import in app file
# so we need to import the app instance, and render_template
from app import app, db
from flask import render_template, redirect, url_for
from models import Task
from datetime import datetime

import forms


@app.route("/")
@app.route("/index")
def index():
    # we create a list of tasks
    tasks = Task.query.all()
    # and we pass them to the index page
    return render_template("index.html", tasks=tasks)

# we can give a list of methods, that are allowed
@app.route("/add", methods=["GET", "POST"])
def add():
    form = forms.AddTaskForm()
    if form.validate_on_submit():
        t = Task(title=form.title.data, date=datetime.utcnow())
        db.session.add(t)
        db.session.commit()
        print("Submitted title", form.title.data)
        # title - property added to add.html
 #       return render_template("add.html", form=form, title=form.title.data)
        # we want to send content of db to index page, so the tasks are listed then
        # and we are automatically moved to the index page after submitting
        return redirect(url_for('index'))
    return render_template("add.html", form=form)