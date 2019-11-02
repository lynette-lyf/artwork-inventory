from flask import Flask, render_template, request, redirect, url_for
import os
from bson import ObjectId
import re

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
    
    filter = request.args.getlist('filter')
    
    all_styles = ['Abstract', 'Abstract Expressionist', 'Contemporary', 'Cubism', 'Expressionism', 'Figurative', 'Geometric', 'Minimalism', 'Modern', 'Nanyang', 'Pop Art', 'Realism', 'Renaissance', 'Surrealism']
    all_types = ['Acrylic', 'Canvas', 'Calligraphy', 'Ink', 'Installation', 'Fabric', 'Oil', 'Paper', 'Painting', 'Portrait', 'Printmaking', 'Sculpture', 'Watercolour']
    
    artworksAndConsigners = conn[DATABASE_NAME]['artworksAndConsigners'].find()
    return render_template('index.template.html', results=artworksAndConsigners, filter=filter, all_styles=all_styles, all_types=all_types)


# CREATE************************************************************************

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
        "type" : type
    })
    
    # redirect back to root url
    return redirect("/")
    
# READ**************************************************************************

@app.route('/')
def search_index():
    search_terms = request.args.get('search-by')
    title = request.args.get('title')
    must_have = request.args.getlist('must-have')
    
    all_types = ['Abstract', 'Abstract Expressionist', 'Contemporary', 'Cubism', 'Expressionism', 'Figurative', 'Geometric', 'Minimalism', 'Modern', 'Nanyang', 'Pop Art', 'Realism', 'Renaissance', 'Surrealism']

    search_criteria = {}
    print (search_criteria)
    if search_terms is not None and search_terms is not "":
        search_criteria["title"] = re.compile(r'{}'.format(search_terms), re.I)

    if len(must_have) > 0:
        search_criteria['all_types'] = {
            '$all' : must_have 
        }
        
    
        
    print (search_criteria)
    # # for display
    # if search_terms is None:
    #     search_terms =""
    
    if search_terms is None:
        search_terms = ""
    
    conn = get_connection()
    cursor = conn[DATABASE_NAME]["artworksAndConsigners"].find(search_criteria).limit(10)
    return render_template("index.template.html", results=cursor, 
        search_terms=search_terms, title=title, all_types=all_types, must_have=must_have)

# UPDATE************************************************************************

@app.route('/edit-artwork/<artwork_id>')
def show_edit_artwork_form(artwork_id):
    conn = get_connection()
    artwork = conn[DATABASE_NAME]['artworksAndConsigners'].find_one({
        '_id': ObjectId(artwork_id)
    })
    
    results = artwork['type']
    all_styles = ['Abstract', 'Abstract Expressionist', 'Contemporary', 'Cubism', 'Expressionism', 'Figurative', 'Geometric', 'Minimalism', 'Modern', 'Nanyang', 'Pop Art', 'Realism', 'Renaissance', 'Surrealism']
    all_types = ['Acrylic', 'Canvas', 'Calligraphy', 'Ink', 'Installation', 'Fabric', 'Oil', 'Paper', 'Painting', 'Portrait', 'Printmaking', 'Sculpture', 'Watercolour']
    
    return render_template('edit_artwork.template.html', artworksAndConsigners=artwork, 
    selected_type = results, all_styles=all_styles, all_types=all_types)
    
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
        '_id': ObjectId(artwork_id)
    }, {
       "image" : image,
        "artist" : artist,
        "title" : title,
        "year" : year,
        "dimensions" : dimensions,
        "medium" : medium,
        "description" : description,
        "type": type 
    })
    
    return redirect("/")
    
    
# DELETE************************************************************************

@app.route('/confirm-delete-artwork/<artwork_id>')
def confirm_delete_artwork(artwork_id):
    
    artwork = conn[DATABASE_NAME]["artworksAndConsigners"].find_one({
        '_id': ObjectId(artwork_id)
    }, {
        "title": 1,
        "artist": 1
    })
    
    return render_template('confirm_delete_artwork.template.html', artworksAndConsigners=artwork)

@app.route('/delete-artwork/<artwork_id>')
def delete_artwork(artwork_id):
    conn[DATABASE_NAME]["artworksAndConsigners"].delete_one({
        '_id': ObjectId(artwork_id)
    })
    
    return redirect('/')

# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)
