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

# we can give a list of methods, that are allowed
@app.route("/about", methods=["GET", "POST"])
def about():
    form = forms.AddTaskForm()
    if form.validate_on_submit():
        print("Submitted title", form.title.data)
        # title - property added to about.html
        return render_template("about.html", form=form, title=form.title.data)
    return render_template("about.html", form=form)