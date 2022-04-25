from email import message
from turtle import title
from flask import render_template
from app import app
from .request import get_movies
# views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    # getting popular movie
    popular_movies = get_movies('popular')
    print(popular_movies)
    title = 'Home - Welcome to the best Movie Review Webdite Online'
    return render_template('index.html', title = title,popular = popular_movies)
  