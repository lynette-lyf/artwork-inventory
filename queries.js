{ "_id" : ObjectId("5db518321c9d440000dc1645"), 
"artist" : "Wong Keen",
"title" : "The Meat Stall",
"year" : "2018",
"dimensions" : "215 x 305 cm",
"medium" : "Acrylic on canvas",
"date_obtained" : "22/10/2019",
"type" : [ "Abstract Expressionist", "Painting", "Acrylic" ],
"location" : "Gallery",
"price" : { "list_price" : "5,000", "selling_price" : "10,000", "best_price" : "8,000" },
"status" : "Available",
"consigner" : { "consigner_name" : "Kelvin Yeo Eng Cheng", "consigner_email" : "yeo_ec@gmail.com", "consigner_mobile" : "93378512" } }


db.listingsAndReviews.find({
    
}).limit(5).pretty()

//filter and projection
//find all listings that have exact 5 beds
//limit : gives most recent IDs
db.listingsAndReviews.find({
    'beds': 5    
}, {'address':1, 'beds':1, 'name':1}).limit(5).pretty()


//find 5 beds or more
//SQL: SELECT beds FROM listingsAndReviews WHERE beds > 4
db.listingsAndReviews.find({
    'beds': {
        $gt: 4
    }    
}, {'beds':1, 'name':1}).limit(5).pretty()


//find
db.listingsAndReviews.find({
    'beds': {
        $gte: 5,
        $lte: 10
    }    
}, {'beds':1, 'name':1}).limit(5).pretty()


db.listingsAndReviews.find({
    'beds': {
        $gt: 4,
        $lt: 11
    },
    'bathrooms': {
        $gt: 1
    }
}, {'beds':1, 'name':1, 'bathrooms':1}).limit(5).pretty()



db.listingsAndReviews.find({
    'beds': {
        $gt: 4,
        $lt: 11
    },
    'bathrooms': {
        $gt: 1
    },
    'address.country': 'Canada'
}, {'beds':1, 'name':1, 'bathrooms':1, 'country': 1}).limit(5).pretty()

//Ameninites must have Internet
db.listingsAndReviews.find({
   'amenities':'Internet'
}, {'amenities': 1, 'name':1}).limit(5).pretty()

//Amenities must have internet and laptop friendly workplace ERROR
db.listingsAndReviews.find({
   'amenities': {
       $all: ['Internet', 'Laptop friendly workplace', 'Wheelchair accessible']
   }
}, {'amenities': 1, 'name':1}).limit(5).pretty()

//$IN = EITHER ONE
db.listingsAndReviews.find({
   'amenities': {
       $in: ['Internet', 'Wifi']
   }
}, {'amenities': 1, 'name':1}).limit(5).pretty()


//AMENITIES MUST NOT HAVE INTERNET OR WIFI USE $NIN
db.listingsAndReviews.find({
   'amenities': {
       $nin: ['Internet', 'Wifi']
   }
}, {'amenities': 1, 'name':1}).limit(5).pretty()


//MOVIES MFLIX DATABASE
db.movies.find({
    'cast': 'Tom Cruise'
},{'title':1,'cast':1}).limit(10).pretty()

db.movies.find({
    'cast': {
        $all: ['Tom Cruise','Cameron Diaz']
    }
},{'title':1,'cast':1}).limit(10).pretty()


db.movies.find({
    'cast':'Tom Cruise'
}).count()


//SORT IN ASCENDING ORDER
db.movies.find({
    'cast': 'Tom Cruise'
},{'title':1,'cast':1}).sort({'title':1}).limit(10).pretty()

//SORTI N DESCENDING ORDER
db.movies.find({
    'cast': 'Tom Cruise'
},{'title':1,'cast':1}).sort({'title':-1}).limit(10).pretty()

//SEARCH FOR TITLES WITH 'RING' case sensitive (REGULAR EXPRESSION)
db.movies.find({
    title:/ring/
},{'title':1}).limit(10).pretty()


//search for titles that contain big R or small R
db.movies.find({
    title:/[Rr]ing/
},{'title':1}).limit(10).pretty()

// TO CLEAR SCREEN: cls



//INSERTING NEW ANIMAL
db.animals.insert({
    name:'Manny',
    breed:'Ragdoll'
})

//INSERT NEW ANIMAL WITH NEW RECORD: MICROCHIP
db.animals.insert({
    name:'Nemo',
    breed:'Tabby',
    microchip:'A1234Z'
})

//FIND BY OBJECT ID (REMEMBER TO PUT _id)
db.animals.find({
    _id: ObjectId("5dad3e4d6de65a133b994a97")
})

//UPDATE NEMO'S BREED FROM TABBY TO NORWEGIAN FOREST
db.animals.update({_id:ObjectId("5dad3e4d6de65a133b994a97")
},{
    $set: {
        breed: 'Norwegian Forest'
    }
})

//DELETE NEMO
db.animals.remove({
    _id: ObjectId("5dad3e4d6de65a133b994a97")
})