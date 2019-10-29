from flask import Flask, render_template, request, redirect, url_for
import os
from bson import ObjectId

import pymongo

MONGO_URI = os.getenv('MONGO_URI')
DATABASE_NAME = 'artworksAndConsigners'

conn = pymongo.MongoClient(MONGO_URI)

def get_connection():
    conn = pymongo.MongoClient(MONGO_URI)
    return conn
    
app = Flask(__name__)

@app.route('/')
def index():
    artworksAndConsigners = conn[DATABASE_NAME]['artworksAndConsigners'].find()
    return render_template('index.template.html', results=artworksAndConsigners)


# CREATE

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
    
    # pass value as ARRAY
    type = request.form.getlist('type')
    
    conn = get_connection()
    conn[DATABASE_NAME]['artworksAndConsigners'].insert({
        "image" : image,
        "artist" : artist,
        "title" : title,
        "year" : year,
        "dimensions" : dimensions,
        "medium" : medium,
        "description" : description,
        
    # pass value as ARRAY
        "type" : type
    })
    
    # redirect back to root url
    return redirect("/")

# UPDATE

@app.route('/edit-artwork/<artwork_id>')
def show_edit_artwork_form(artwork_id):
    conn = get_connection()
    artwork = conn[DATABASE_NAME]['artworksAndConsigners'].find_one({
        '_id': ObjectId(artwork_id)
    })
    
    results = artwork['type']
    
    return render_template('edit_artwork.template.html', artworksAndConsigners=artwork, types = results)
    
@app.route("/edit-artwork/<artwork_id>", methods=['POST'])
def process_edit_artwork_form(artwork_id):
    image = request.form.get('image')
    artist = request.form['artist']
    title = request.form['title']
    year = request.form['year']
    dimensions = request.form['dimensions']
    medium = request.form['medium']
    description = request.form['description']
    
    type = request.form.getlist('type')
    
    conn = get_connection()
    conn[DATABASE_NAME]["artworksAndConsigners"].update({
        '_id': 'ObjectId(artwork_id)'
    }, {
       "image" : image,
        "artist" : artist,
        "title" : title,
        "year" : year,
        "dimensions" : dimensions,
        "medium" : medium,
        "description" : description,
        
    # pass value as ARRAY
        "type" : type
    })
    
    return redirect("/")



# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)
