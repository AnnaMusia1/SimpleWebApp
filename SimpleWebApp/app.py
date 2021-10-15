from flask import Flask
from flask_sqlalchemy import SQLAlchemy


__name__ = "__main__"
# The file app.py will be an entry point for our webapp application.
# We will execute it from the command line.

# In situation like this, there is a special variable __name__,
# and python automatically assigns a value to it -> __main__

# Initialize the app instance
app = Flask(__name__)
# config is necessary for working the {{ form.csrf_token() }} in about file
app.config["SECRET_KEY"] = "secret-key"
# we also need a config for SQLalchemy
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"

db = SQLAlchemy(app)

# import all content from routes file
from routes import *

# # decorator to tell our server, that at this path we want to run this function
# # we could use multiple routes for the same function, and this will update the server automatically@
# @app.route("/")
# @app.route("/index")
# def index():
# # we can also add some html
# #    return "<h1>Hello</h1> World!"
#
# # we can also start a template with html code - render_template with the name of the file
# # the file needs to be in "templates" folder
#
# # current_title - variable to use in html file (Jinja template in flask)
#     return render_template("index.html", current_title='Custom title')
#
# @app.route("/about")
# def about():
#     return render_template("about.html")





if __name__ == "__main__":
    app.run(debug=True)
    # setting debug argument to true, gives us some debug functionality from flask
