from flask import render_template,request,redirect,url_for,abort
from . import main
from .forms import ReviewForm, UpdateProfile
from ..models import User
from flask_login import login_required,current_user
from .. import db,photos
import markdown2  
from ..request import get_pitches;



# Views

@main.route('/')
# @login_required
def index():

    '''
    View root page function that returns the index page and its data

    '''

    # Getting popular movie
   
        
    return render_template('index.html')

@main.route('/pitches')
def pitches():

    '''
    View movie page function that returns the movie details page and its data
    '''
    
    # reviews = Review.get_reviews(movie.id)
    pitches=get_pitches()

    return render_template('pitches.html',pitches=pitches)



