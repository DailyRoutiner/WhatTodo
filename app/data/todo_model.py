from app import db


class Todo(db.Model):
    __tablename__ = 'todolist'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(300), nullable=False)
    status = db.Column(db.Boolean, nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)

    email = db.Column(db.String(255), nullable=False, unique=True)
    email_confirmed_at = db.Column(db.DateTime())
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)

