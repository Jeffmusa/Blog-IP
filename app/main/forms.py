from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required




class CommentForm(FlaskForm):

    user = StringField('Your name',validators=[Required()])

    comment = TextAreaField('Your comment',validators=[Required()])
    
    submit = SubmitField('Comment')


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')   