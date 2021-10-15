# models for data base model
from app import db


class Task(db.Model):
    # type - Integer, primary_key: keys will be in order
    id = db.Column(db.Integer, primary_key=True)
    # type - string with length of 100, nullable: title can't be empty
    title = db.Column(db.String(100), nullable=False)
    date = db.Column(db.Date, nullable=False)

    # function to represent the instance of db (it prints the instance )
    def __repr__(self):
        return f"{self.title} created on {self.date}"