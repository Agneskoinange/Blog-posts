from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
    

class User(UserMixin, db.Model):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    about = db.Column(db.String(255))
    avatar = db.Column(db.String())
    password_encrypt=db.Column(db.String(128))
    pitches = db.relationship('Pitches', backref='user', lazy='dynamic')
    like = db.relationship('UpVote',backref='user',lazy='dynamic')
    dislike = db.relationship('DownVote',backref='user',lazy='dynamic')
    comments = db.relationship('Comments', backref='comments', lazy='dynamic')


    @property   #write-only
    def password(self):
        raise AttributeError('You can only read this attribute')

    @password.setter
    def password(self, password):
        self.password_encrypt = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_encrypt, password)

    def __repr__(self):
        return f'User{self.username}'


class Pitches(db.Model):
    __tablename__='pitches'
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(255))
    text = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    posted = db.Column(db.DateTime, default=datetime.utcnow)
    comments = db.relationship('Comments', backref='pitch', lazy='dynamic')
    like = db.relationship('UpVote',backref='pitch',lazy='dynamic')
    dislike = db.relationship('DownVote',backref='pitch',lazy='dynamic')
    

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_category(cls, category):
        pitches = Pitches.query.filter_by(category=category).all()
        return pitches

    def __repr__(self):
        return f'Pitches{self.text}'


class UpVote(db.Model):
    __tablename__ = 'likes'
    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_likes(cls,id):
        like = UpVote.query.filter_by(pitch_id=id).all()
        return like

    def __repr__(self):
        return f'{self.user_id}:{self.pitch_id}'


class DownVote(db.Model):
    __tablename__ = 'dislikes'

    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))
    

    def save(self):
        db.session.add(self)
        db.session.commit()
    @classmethod
    def get_dislikes(cls,id):
        dislike = DownVote.query.filter_by(pitch_id=id).all()
        return dislike

    def __repr__(self):
        return f'{self.user_id}:{self.pitch_id}'
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)


class Comments(db.Model):
    __tablename__='comments'
    id = db.Column(db.Integer, primary_key=True)
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))
    comment = db.Column(db.String(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls,pitch_id):
        comments = Comments.query.filter_by(pitch_id=pitch_id)
        return comments
    
    def __repr__(self):
        return f'Comments:{self.comment}'