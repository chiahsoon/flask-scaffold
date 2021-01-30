"""
This folder (/models) will contain the definition for all the data access objects.
"""
from models.user import User

'''
--------------------------------------------------------------------------------------------------------------------
Explanation for the relationships. For example,

    class Organisation(db.Model)
        id = db.Column(db.String, primary_key=True, nullable=False)
        projects = db.relationship('Project', backref='org')

    class Project(db.Model):
        id = db.Column(db.String, primary_key=True, nullable=False)
        org_id = db.Column(db.Integer, db.ForeignKey('organisation.id'), primary_key=True)

* This means that that project objects will be able to do something like my_project.org in order to get the
organisation object.
* This also means that the org_id attribute in Project is just that - an integer id column, not the organisation
object.
* We can also do my_organisation.projects to find a list of projects associated with my_organisation
* If it is a one-to-one, we can use the argument uselist=False to enforce that there should be only 1.
--------------------------------------------------------------------------------------------------------------------
'''

'''
--------------------------------------------------------------------------------------------------------------------
https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/
Example of model file:

from extensions import db

class Label(db.Model):
    # 1(Task)-to-Many(Label)
    task_id = db.Column(db.String(80), db.ForeignKey('task.id'), primary_key=True, nullable=False)
    # 1(Task)-to-Many(User)
    user_id = db.Column(db.String(80), db.ForeignKey('user.id'), primary_key=True, nullable=False)

    label_data = db.Column(db.JSON(), nullable=False)   # JSON
    created_at = db.Column(db.DateTime(), nullable=False)

    def __repr__(self):
        return f"<Label | task_id : {self.task_id} | user_id : {self.user_id}>"

    def to_response(self):
        return {
            "task_id": self.task_id,
            "user_id": self.user_id,
            "label_data": self.label_data,
            "created_at": self.created_at
        }
--------------------------------------------------------------------------------------------------------------------
'''
