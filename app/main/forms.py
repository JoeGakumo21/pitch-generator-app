from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required

class ReviewForm(FlaskForm):

    title = StringField('Review title',validators=[Required()])
    review = TextAreaField('Movie review')
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')


class PitchForm(FlaskForm):
  title = StringField('Pitch title')
  category = SelectField("Choose Category",choices=[('Brand','Personal brand'),('Product','Product'),('Project','Project'),('Investor','Investor')])
  pitch = TextAreaField('Your Pitch',validators=[Required()])
  submit = SubmitField('Submit')


class CommentForm(FlaskForm):
  comment = TextAreaField('Your Comment',validators=[Required()])
  submit = SubmitField('Submit') 