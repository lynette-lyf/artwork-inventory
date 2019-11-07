from flask import Flask, render_template, request, redirect, url_for, flash
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
    
all_styles = ['Abstract', 'Abstract Expressionist', 'Contemporary', 'Cubism', 'Expressionism', 'Figurative', 'Geometric', 'Minimalism', 'Modern', 'Nanyang', 'Pop Art', 'Realism', 'Renaissance', 'Surrealism']
all_types = ['Acrylic', 'Canvas', 'Calligraphy', 'Ink', 'Installation', 'Fabric', 'Oil', 'Paper', 'Painting', 'Portrait', 'Printmaking', 'Sculpture', 'Watercolour']
        
app = Flask(__name__)

# READ**************************************************************************

@app.route('/')
def index():
    search_terms = request.args.get('search-by')
    filter = request.args.getlist('filter')
   
    
    search_criteria = {}
    
    if search_terms is not None and search_terms is not "":
        search_criteria["title"] = re.compile(r'{}'.format(search_terms), re.I)
        
    if len(filter) > 0:
        search_criteria["type"] = {
            '$all' : filter
        }
   
    
    if search_terms is None:
        search_terms = ""
    
    conn = get_connection()
    artworksAndConsigners = conn[DATABASE_NAME]['artworksAndConsigners'].find(search_criteria)
    return render_template('index.template.html', results=artworksAndConsigners, search_terms=search_terms, filter=filter, all_styles=all_styles, all_types=all_types)

# VIEW INDIVIDUAL ARTWORK*******************************************************
@app.route('/artwork/<artwork_id>')
def show_artwork(artwork_id):
    
    artworksAndConsigners = conn[DATABASE_NAME]["artworksAndConsigners"].find_one({
        '_id': ObjectId(artwork_id)
    }, {
        "image" : 1,
        "artist" : 1,
        "title" : 1,
        "year" : 1,
        "dimensions" : 1,
        "medium" : 1,
        "description" : 1,
        "type": 1,
        "votes": 1,
        "comments": 1
    })
    
    return render_template('show_artwork.template.html', artworksAndConsigners=artworksAndConsigners)

# SHOW COMMENTS & COMMENT FORM ON EACH INDIVIDUAL ARTWORK***********************

@app.route('/artwork/<artwork_id>', methods=['POST'])
def process_add_comment(artwork_id):
    comments = {
    'comment_name': request.form.get('comment_name'),
    'comment_comment' : request.form.get('comment_comment')    
    }
    
    
    artworksAndConsigners = conn[DATABASE_NAME]['artworksAndConsigners'].update(
        {
            "_id": ObjectId(artwork_id)
        }, 
        {'$push': {
            'comments': comments
        }
            
        })

    return redirect(request.url)

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
    votes = request.form['votes']
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
        "type" : type,
        "votes": votes
    })
    
    return redirect("/")

# UPDATE************************************************************************

@app.route('/edit-artwork/<artwork_id>')
def show_edit_artwork_form(artwork_id):
    conn = get_connection()
    artwork = conn[DATABASE_NAME]['artworksAndConsigners'].find_one({
        '_id': ObjectId(artwork_id)
    })
    
    results = artwork['type']
   
    return render_template('edit_artwork.template.html', artworksAndConsigners=artwork, 
    selected_type=results, all_styles=all_styles, all_types=all_types)
    
@app.route("/edit-artwork/<artwork_id>", methods=['POST'])
def process_edit_artwork_form(artwork_id):
    image = request.form.get('image')
    artist = request.form['artist']
    title = request.form['title']
    year = request.form['year']
    dimensions = request.form['dimensions']
    medium = request.form['medium']
    description = request.form['description']
    votes = request.form['votes']
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
        "type": type,
        "votes": votes
    })
    
    return redirect("/")
    
# FAVOURITE FUNCTION************************************************************
@app.route('/', methods=["POST"])
def process_votes(artwork_id):
    votes = int(request.form['votes']) + 1

    
    conn = get_connection()
    conn[DATABASE_NAME]["artworksAndConsigners"].update({
        '_id': ObjectId(artwork_id)
    }, {
        "votes": votes
    })
    
    return redirect('/')
    
# DELETE************************************************************************

@app.route('/confirm-delete-artwork/<artwork_id>')
def confirm_delete_artwork(artwork_id):
    
    artwork = conn[DATABASE_NAME]["artworksAndConsigners"].find_one({
        '_id': ObjectId(artwork_id)
    }, {
        "image" : 1,
        "artist" : 1,
        "title" : 1,
        "year" : 1,
        "dimensions" : 1,
        "medium" : 1,
        "description" : 1,
        "type": 1
    })
    
    return render_template('confirm_delete_artwork.template.html', artworksAndConsigners=artwork)

@app.route('/delete-artwork/<artwork_id>')
def delete_artwork(artwork_id):
    conn[DATABASE_NAME]["artworksAndConsigners"].delete_one({
        '_id': ObjectId(artwork_id)
    })
    
    return redirect('/')
    
# INFORMATION FOR ART STYLES****************************************************
@app.route('/information/artstyles')
def art_style():
    conn = get_connection()
    styles = conn[DATABASE_NAME]['artstyles'].find()
    return render_template('artstyles.template.html', results=styles)
    


# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)
