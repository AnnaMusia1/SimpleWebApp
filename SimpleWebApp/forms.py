# import from flask form module
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


# creating the form
# we use classes, every class will be extended by FlaskForm class
class AddTaskForm(FlaskForm):
     # input field
    title = StringField("Title", validators=[DataRequired()])
     # sumbit button with the label "Submit"
    submit = SubmitField("Submit")

class DeleteTaskForm(FlaskForm):
    submit = SubmitField("Delete")