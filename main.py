from flask import Flask, request, render_template, url_for,redirect
import random
from database import *
from textblob import TextBlob

app = Flask(__name__)
app.config['SECRET_KEY'] = 'changeme'

# TODO: Add all of the routes you want below this line!

@app.route('/', methods=['GET','POST'])  # '/' for the default page
def home():
  if request.method=='GET':
	  return render_template('home.html')
  else:
    feedback=request.form['feedback']
    blob1=TextBlob(feedback)
    if (blob1.sentiment.polarity<0):
      return render_template("home.html")  

@app.route('/about_us')
def about_us():
  return render_template('about_us.html')

@app.route('/shop')
def shop():
  return render_template('shop.html', movies=query_all())

@app.route('/buying_item')
def buying_item():
  return render_template('buying_item.html')

@app.route('/review', methods=['Get','POST'])
def review():
  return render_template('review.html')  
  
@app.route('/add_product', methods=['GET','POST'])
def add_product():
  if request.method=='GET':
	  return render_template('add_product.html')
  else:
    pic_link=request.form['pic_link']
    director=request.form['director']
    movie_name=request.form['movie_name']
    release_year=request.form['release_year']
    price=request.form['price']
    description=request.form['description']
    create_movie( pic_link, director,movie_name, release_year, price, description)
    return render_template('shop.html', movies=query_all())

@app.route('/delete/<int:id>')
def delete(id):
  delete_movie(id)
  return redirect(url_for('shop')) 
   
if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
		host='0.0.0.0',  # EStablishes the host, required for repl to detect the site
		port=random.randint(2000, 9000),  # Randomly select the port the machine hosts on.
    debug=True
	)

