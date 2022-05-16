from . import db,login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin,current_user


class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    pass_secure = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    blog = db.relationship('Blog',backref='user', lazy='dynamic')
    comment = db.relationship('Comment', backref='user', lazy='dynamic')

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)
    
    def __repr__(self):
        return f'User {self.username}'


class Blog(db.Model):
     __tablename__ = 'blog'
     id = db.Column(db.Integer,primary_key = True)
     username = db.Column(db.String(255),index = True)
     blog = db.Column(db.String(300),index =True)
     title = db.Column(db.String(100), index = True)
     user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
     comment = db.relationship('Comment', backref='pitch', lazy='dynamic')

     def save_p(self):
        db.session.add(self)
        db.session.commit()

     def delete(self):
        db.session.delete(self)
        db.session.commit()

     def get_blog(id):
        blog = Blog.query.filter_by(id=id).first()
        return blog

     def __repr__(self):
        return f'Blog {self.title}'

class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.Text(),nullable = False)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'),nullable = False)
    blog_id = db.Column(db.Integer,db.ForeignKey('blog.id'),nullable = False)
    

    def save_c(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.remove(self)
        db.session.commit()

    @classmethod
    def get_comments(cls,blog_id):
        comments = Comment.query.filter_by(blog_id=blog_id).all()
        return comments

    
    def __repr__(self):
        return f'comment:{self.comment}'
    
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))