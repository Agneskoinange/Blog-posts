from app.request import get_quotes
from . import main
from flask import render_template,redirect,url_for,abort,flash,request
from flask_login import current_user, login_required
from .forms import CreateBLog,UpdateProfile,CommentForm
from ..models import User,Blog,Comment
from .. import db

@main.route('/')
def index():
   return render_template('index.html')

@main.route('/home')
@login_required
def home():
   return render_template('home.html')

@main.route('/random_quotes')
@login_required
def random():
   quote = get_quotes()
   return render_template('random.html',quote = quote)


@main.route('/create_new', methods = ['POST','GET'])
@login_required
def new_blog():
    form =CreateBLog()
    if form.validate_on_submit():
        title = form.title.data
        blog = form.blog.data
        name = form.name.data
        new_pitch_object = Blog(username=name,user_id=current_user._get_current_object().id,blog=blog,title=title)
        new_pitch_object.save_p()
        return redirect(url_for('main.blog'))
        
    return render_template('blog.html', form = form)

@main.route('/blog')
@login_required
def blog():
    blog = Blog.query.all()
    return render_template('new_blog.html', blog = blog)

@main.route('/blog/<blog_id>/update', methods = ['GET','POST'])
@login_required
def updateblog(blog_id):
    blog = Blog.query.get(blog_id)
    if blog.user != current_user:
        abort(403)
    form = CreateBLog()
    if form.validate_on_submit():
        blog.username = form.name.data
        blog.title = form.title.data
        blog.blog = form.blog.data
        db.session.commit()
        flash("You have updated your Blog!")
        return redirect(url_for('main.blog',id = blog.id)) 
    if request.method == 'GET':
        form.name.data = blog.username
        form.title.data = blog.title
        form.blog.data = blog.blog
    return render_template('blog.html', form = form)

@main.route('/blog/<blog_id>/delete', methods = ['POST'])
def delete_post(blog_id):
    blog = Blog.query.get(blog_id)
    if blog.user != current_user:
        abort(403)
    blog.delete()

    flash("You have deleted your Blog succesfully!")
    return redirect(url_for('main.blog'))


@main.route('/comment/<int:blog_id>', methods = ['POST','GET'])
def comment(blog_id):
    form = CommentForm()
    blog = Blog.query.get(blog_id)
    all_comments = Comment.query.filter_by(blog_id = blog_id).all()
    if form.validate_on_submit():
        comment = form.comment.data 
        blog_id = blog_id
        user_id = current_user._get_current_object().id
        new_comment = Comment(comment = comment,user_id = user_id,blog_id = blog_id)
        new_comment.save_c()
        return redirect(url_for('.comment', blog_id = blog_id))
    return render_template('comment.html', form =form, blog = blog,all_comments=all_comments)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('main.profile',uname=user.username))

    return render_template('profile/update.html',form =form)