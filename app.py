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
    artworksAndConsigners = conn[DATABASE_NAME]['artworksAndConsigners'].find()
    return render_template('index.template.html', results=artworksAndConsigners)


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
    
# READ**************************************************************************

@app.route('/')
def index_search():
    search_terms = request.args.get('search-by')
    title = request.args.get['title']
    artist = request.args.get['artist']
    
#     # countries = ["Singapore", "Canada", "New Zealand", "Malaysia", "Ireland"]
#     # amentities = ["Internet", "Washer", "Waterfront","Step-free access"]

    search_criteria = {}
    print (search_criteria)
    if search_terms is not None and search_terms is not "":
        search_criteria["title", "artist"] = re.compile(r'{}'.format(search_terms), re.I)
        # search_criteria["artist"] = re.compile(r'{}'.format(search_terms), re.I)

#     # if country != None and country != "Any":
#     #     search_criteria['address.country'] = country 
        
#     # if len(must_have) > 0:
#     #     search_criteria['amenities'] = {
#     #         '$all' : must_have 
#     #   }
        
    
        
    print (search_criteria)
#     for display
#     if search_terms is None:
#         search_terms =""
    
    if search_terms is None:
        search_terms = ""
    
    conn = get_connection()
    cursor = conn[DATABASE_NAME]["artworksAndConsigners"].find(search_criteria)
    return render_template("index.template.html", results=cursor, 
        search_terms=search_terms, title=title, artist=artist) 
        
#         # countries=countries,
#         # amentities=amentities, must_have=must_have)

# UPDATE************************************************************************

@app.route('/edit-artwork/<artwork_id>')
def show_edit_artwork_form(artwork_id):
    conn = get_connection()
    artwork = conn[DATABASE_NAME]['artworksAndConsigners'].find_one({
        '_id': ObjectId(artwork_id)
    })
    
    results = artwork['type']
    all_types = ['Abstract', 'Abstract Expressionist', 'Renaissance', 'Impressionism', 'Painting', 'Acrylic']

    return render_template('edit_artwork.template.html', artworksAndConsigners=artwork, 
    selected_type = results, all_types=all_types)
    
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
        "type": type 
    })
    
    return redirect("/")
    
    
# DELETE************************************************************************

@app.route('/confirm-delete-artwork/<artwork_id>')
def confirm_delete_artwork(artwork_id):
    artist = request.form.get('artist')
    title = request.form.get('title')
    artwork = conn[DATABASE_NAME]["artworksAndConsigners"].find_one({
        '_id': 'ObjectId(artwork_id)',
    }, {
        "title": title,
        "artist": artist
    })
    
    return render_template('confirm_delete_artwork.template.html', artworksAndConsigners=artwork)

@app.route('/delete-artwork/<artwork_id>')
def delete_artwork(artwork_id):
    conn[DATABASE_NAME]["artworksAndConsigners"].delete_one({
        '_id': 'ObjectId(artwork_id)'
    })
    
    return redirect('/')

# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)
