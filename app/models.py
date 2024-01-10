from app import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from app import login


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(80),unique=True,nullable=False)
    email = db.Column(db.String(120),unique=True,nullable=True)
    password = db.Column(db.String(128))
    password_hash = db.Column(db.String(128))
    post = db.relationship('Post',backref='author',lazy='dynamic')
    # comment = db.relationship('Comment',backref='author',lazy='dynamic')

    @property
    def password(self):
        raise AttributeError('密码属性不可读')

    def set_password(self,password):
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return '<User %r>' % self.username



class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(80),nullable=False)
    body = db.Column(db.Text,nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    # comment = db.relationship('Comment',backref='post',lazy='dynamic')

    def __repr__(self):
        return '<Post %r>' % self.title