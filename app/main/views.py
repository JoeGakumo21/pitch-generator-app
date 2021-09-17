from flask import render_template,request,redirect,url_for,abort
from . import main
from .forms import ReviewForm, UpdateProfile
from ..models import User
from flask_login import login_required,current_user
from .. import db,photos
import markdown2  




# Views

@main.route('/')
# @login_required
def index():

    '''
    View root page function that returns the index page and its data

    '''

    # Getting popular movie
   
        
    return render_template('index.html')


@main.route('/pitch')
def pitches():
  pitches = Pitch.query.all()
  brand = Pitch.query.filter_by(category='Brand').all()
  product = Pitch.query.filter_by(category='Product').all()
  project = Pitch.query.filter_by(category='Project').all()
  investor = Pitch.query.filter_by(category='Investor').all()

  return render_template('pitch.html',pitches=pitches,brand=brand,product=product,project=project,investor=investor)  



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

    







