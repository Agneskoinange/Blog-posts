from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField
from wtforms.validators import DataRequired


class CreateBLog(FlaskForm):
    name = StringField('Your Name',validators=[DataRequired()])
    title = StringField('Title',validators =[DataRequired()])
    blog = TextAreaField('Blog',validators =[DataRequired()])
    submit = SubmitField('Submit BLog')

class CommentForm(FlaskForm):
    comment = TextAreaField('Leave a comment',validators=[DataRequired()])
    submit = SubmitField('Comment')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [DataRequired()])
    submit = SubmitField('Submit')