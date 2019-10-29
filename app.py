from flask import Flask, render_template, request, redirect, url_for
import os

import pymongo

# 1. Retrieve the environment variables
# MONGO_URI = os.getenv('MONGO_URI')
# DATABASE_NAME = 'artworksAndConsigners'

MONGO_URI = "mongodb+srv://admin:pw@gallery-cwjwv.mongodb.net/test?retryWrites=true&w=majority"
DATABASE_NAME = "artworksAndConsigners"
conn = pymongo.MongoClient(MONGO_URI)

# 2. Create the connection
def get_connection():
    conn = pymongo.MongoClient(MONGO_URI)
    return conn
    
app = Flask(__name__)

@app.route('/')
def index():
    artworksAndConsigners = conn[DATABASE_NAME]['artworksAndConsigners'].find()
    return render_template('index.template.html', results=artworksAndConsigners)


@app.route('/add-artwork')
def show_add_artwork_form():
    return render_template('add_artwork.template.html')

@app.route('/add-artwork', methods=['POST'])
def process_add_artwork_form():
    image = request.form.get('image')
    artist = request.form['artist']
    title = request.form['title']
    year = request.form['year']
    dimensions = request.form['dimensions']
    medium = request.form['medium']
    description = request.form['description']
    type = request.form['type']
    
    conn = get_connection()
    conn[DATABASE_NAME]['artworksAndConsigners'].insert({
        "image" : image,
        "artist" : artist,
        "title" : title,
        "year" : year,
        "dimensions" : dimensions,
        "medium" : medium,
        "description" : description,
        "type" : type
    })
    
    # redirect back to root url
    return redirect("/")



# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)
