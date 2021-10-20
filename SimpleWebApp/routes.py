# as it's not a best practise to keep all the code in one file, we create a separate file for routes
# then, we will keep the routes here, and all the content import in app file
# so we need to import the app instance, and render_template
from app import app, db
# flash and get_flashed_messages methods are convenient way to display some information on our webpages (f.e alert messages)
from flask import render_template, redirect, url_for, flash, get_flashed_messages
from models import Task
from datetime import datetime

# import models
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

        # before redirect to index we want to display some message that the task was saved
        flash("Task added to the database")

        # we want to send content of db to index page, so the tasks are listed then
        # and we are automatically moved to the index page after submitting
        return redirect(url_for('index'))
    return render_template("add.html", form=form)


@app.route("/edit/<int:task_id>", methods=["GET", "POST"])
def edit(task_id):
    # if we searching for primary key, we use the .get() method
    task = Task.query.get(task_id)
    form = forms.AddTaskForm()

    # we make sure the task exists:
    if task:
        # we already have a task, and we know, that the task exists, we want to update the task
        # and the form was validate on submit:
        if form.validate_on_submit():
            task.title = form.title.data
            task.date = datetime.utcnow()
            db.session.commit()
            flash("Task has been updated")
            return redirect(url_for("index"))
        # but, if we don't have the form validated on submit:
        # then we continue to update the form title and render the html for edit

        # form is fulfilled with the info from task
        form.title.data = task.title
        # we return the edit template, where we pass the form with the task's info and task id
        return render_template("edit.html", form=form, task_id=task_id)
    else:
        flash("Task not found")
    return redirect(url_for('index'))


@app.route("/delete/<int:task_id>", methods=["GET", "POST"])
def delete(task_id):
    task = Task.query.get(task_id)
    form = forms.DeleteTaskForm()

    if task:
        # if the "delete" was clicked
        if form.validate_on_submit():
            db.session.delete(task)
            db.session.commit()
            flash("Task has been deleted")
            return redirect(url_for("index"))
        # so long, that the "delete isn't clicked"
        return render_template("delete.html", form=form, task_id=task_id, title=task.title)
    else:
        flash("Task not found")
    return redirect(url_for("index"))
