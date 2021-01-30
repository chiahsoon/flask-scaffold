from utilities import db


class User(db.Model):
    id = db.Column(db.String(80), primary_key=True, nullable=False)
    username = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(256), nullable=False)
    name = db.Column(db.String(120), nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False)
    updated_at = db.Column(db.DateTime(), nullable=False)

    def __repr__(self):
        return f"<User {self.id} | {self.username} ({self.name}) ({self.email}) >"

    def to_dict(self):
        return {
            "username": self.username,
            "email": self.email,
            "name": self.name,
            "id": self.id,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
