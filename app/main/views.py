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
   
        
    return render_template('pitches.html')

@main.route('/pitches')
def pitches():

    '''
    View movie page function that returns the movie details page and its data
    '''
    title="Welcome here"
    # reviews = Review.get_reviews(movie.id)
    

    return render_template('pitches.html',title=title)



