from flask import render_template,request,redirect,url_for,abort
from . import main
from flask_login import login_required,current_user
from .. import db,photos
from .forms import  UpdateProfile,PitchForm,CommentForm
from ..models import User,Pitch,Comment



# Views

@main.route('/')
@login_required
def index():

    '''
    View root page function that returns the index page and its data

    '''

    # Getting popular movie

    return render_template('index.html')


@main.route('/pitch')
def pitches():
  pitches = Pitch.query.all()
  Xactly = Pitch.query.filter_by(category='Xactly').all()
  product = Pitch.query.filter_by(category='Product').all()
 

  return render_template('pitch.html',pitches=pitches,Xactly=Xactly,product=product)  



@main.route('/user/<uname>')
@login_required
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

        return redirect(url_for('.profile',uname = user.username))

    return render_template('profile/update.html',form = form)    



@main.route('/user/<uname>/update/pic',methods = ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname = uname))


@main.route('/pitch/new',methods = ['GET','POST'])
@login_required
def new_pitch():
  form = PitchForm()

  if form.validate_on_submit():
    title=form.title.data
    category = form.category.data
    pitch = form.pitch.data
    # author = current_user
    new_pitch = Pitch(title=title,category=category,pitch=pitch)

    db.session.add(new_pitch)
    db.session.commit()

    return redirect(url_for('main.pitches',id=new_pitch.id))

  return render_template('create_pitch.html',title='Add Your Pitch',pitch_form=form)

@main.route('/comments/<int:id>',methods=['GET','POST'])
def comment_review(id):
  comment = CommentForm()
  pitch=Pitch.query.get(id)

  if comment.validate_on_submit():
    content = comment.comment.data
    
    new_post = Comment(comment=content,title=pitch.id)

    db.session.add(new_post)
    db.session.commit()  
    
  post = 'Post Your Comment'
  user=User.query.get(id)
  comments = Comment.query.filter_by(title=pitch.id).all()  
  if pitch is None:
    abort(404)
  return render_template('comments.html',comment_form=comment,post=post,comments=comments,pitch=pitch,user=user)          



