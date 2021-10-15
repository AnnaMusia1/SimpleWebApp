# as it's not a best practise to keep all the code in one file, we create a separate file for routes
# then, we will keep the routes here, and all the content import in app file
# so we need to import the app instance, and render_template
from app import app
from flask import render_template

import forms


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    form = forms.AddTaskForm()
    return render_template("about.html", form=form)