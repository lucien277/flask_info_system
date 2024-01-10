from app import db

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(80),unique=True,nullable=False)
    email = db.Column(db.String(120),unique=True,nullable=True)
    password = db.Column(db.String(120),nullable=False)
    post = db.relationship('Post',backref='author',lazy='dynamic')
    # comment = db.relationship('Comment',backref='author',lazy='dynamic')

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