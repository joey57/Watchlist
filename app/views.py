from email import message
from flask import render_template
from app import app
# views
@app.route('/movie/<int:movie_id>')
def movie(movie_id):
  '''
  view root page function that return the index page and its data 
  '''
  return render_template('movie.html', id = movie_id)
  