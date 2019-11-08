# Artshack Database
## Stream Three Project: Data Centric Development - Code Institute
This web application serves as a database index of artwork archives contributed by users of the public, for users – be it for recreational or educational purposes. The website aims to act as a platform that encourages the art community to grow, thrive and actively promote their favourite artworks from their favourite artists, allowing other users to discover these artists.
This project also intends to act as an extended feature of my Stream One Project: User-Centric Frontend Development, an art gallery website titled ‘Artshack’.
https://lynette-lyf.github.io/artshack/
## Demo
A live demo can be found here.
https://lyfartshackdb.herokuapp.com/
## UX
The use of the monotone colour scheme in the design of the website brings the spotlight to the artwork images. As a user, browsing through multiple images of artworks can be too visually stimulating and exhausting hence I intend to keep the design of the website simple, minimalistic and easy on the eyes.
The use of icons throughout the website elevates the interface in a way that makes it user-friendly and effective in communicating the purpose of each function.
Art collectors, art enthusiasts, art students and practitioners may find the website useful for discovering new artworks, art styles and artists for recreational or educational purposes. They may also like to contribute to the website by uploading their favourite artworks to this platform for the public to view and leave a comment on it. They are also able to make changes to the artwork archive entry in case there are any discrepancies in the artwork details, or even delete the archive entry if they wish to. The general public may also find the website useful in broadening their knowledge or interest in fine art.
## Technologies
1.	HTML
2.	CSS
3.	Bootstrap (4.3.1)
4.	Python (3.6)
5.	Jinja2 (2.10.3)
6.	Flask (1.1.1)
7.	MongoDB
8.	Font Awesome (4.7.0)
9.	Google Fonts API
## Features
The web application achieves these four basic functions of a database, namely CRUD –  an acronym for the four basic types of SQL commands: Create , Read , Update , Delete.
These functions allows users to perform the following features:
1.	Create
a)	Add a new artwork archive to the database with the following details:
-Artwork image
-Title
-Artist
-Year
-Dimensions
-Medium
-Description
		b) Create a comment on each individual artwork
2.	Read
a)	Find artworks that matches the queries such as having a searchbox for artwork titles with a dropdown menu that allows the user to filter their searches via art style or type by ticking on the checkboxes.
3.	Update – Edit the archived artwork details in the database
4.	Delete – Delete the archived artwork
### Features Left to Implement
•	Fixing the functionality of the upvote button so that will have a +1 increment each time a user clicks on it.
•	Improve the layout of the style and type filters in the dropdown menu and in the ‘Update’ artworks form as well as its responsiveness for screen widths < 1920px
•	Allow users to upload image files to the website, instead of having to upload the image URL or convert their image to a URL
•	Add advanced validators to the forms that are able to detect whether the user is placing the correct numerical input for each input box (e.g. Dimensions cannot be in other units of measurement)
## Testing
#### 1. Create:
**•	Add a new artwork archive to the database**

All the form input boxes are able to fetch data to the database when the user fills up the form and press the submit button. There is also a validator for each field to prevent the user from submitting an empty field, however, it has limitations as it is unable to detect whether the user has placed in the correct field for each type of input box. (e.g. Dimensions can only be in centimetres, shown as ‘cm’ and always have the ‘by’ symbol x, between each measurement, and cannot be in other units of measurement)

However, a 650-character limit is placed in the ‘Description’ input box, and users can only enter a four digit integer from 1000 to 2019 for the ‘Year’ input box.

Selecting the style or type checkboxes are optional and more than one checkboxes can be selected at a time.

**•	Create a comment on each individual artwork**
The comment form is successful in fetching input data to the database with both the commenter’s name and comment. Every single comment entry made on each individual artwork is added to the database as an object in an array called ‘comments’, under the specific object ID given for each artwork. Once the user has submitted the comment, the comments will show up after the page has automatically refreshed.

#### 2. Read:
**•	Searchbox for artwork titles**
The search function is able to perform its function by filtering out the results according to the search query input using the regular expression, which would ignore any case sensitivity and parse in the search query as a string – ignoring any escape characters that could potentially interfere with the searchbox.

**•	Dropdown menu with checkboxes to filter the queries**
In addition to the search function, the user has the ability to narrow down their searches by filtering out the results based on the each tag that the artwork has been assigned to. The tags are based on the artwork’s style or type. Upon clicking on the carat icon (down arrow) in the searchbox, the dropdown menu with the checkboxes will appear, allow the user to select them. Overall, the user is able to either type their search query input in the searchbox, filter the results via checking the checkboxes or stack their search criteria using both functions.

#### 3. Update:
**•	Edit the details of the existing artworks**
The default details of the existing artworks from the database will reflect in the input form as well as checked checkboxes (if any). This is to ensure that the user is aware of the changes they are making to the artwork archive. Once the form is submitted, the data of the artwork archive will be updated to the database.

#### Delete:
**•        Delete existing artworks**
The delete function prompts the user to think twice before proceeding to delete the artwork archive off the database. If the user agrees to delete, the artwork archive entry will be remove from the website and database completely. If the user changes their mind and decided to cancel the deletion, they will be redirected to the index page.

To ensure compatibility and responsiveness, the site was tested across multiple browsers such as Chrome, Firefox, Safari and Internet Explorer and on multiple android devices - Galaxy S5, Pixel 2, Pixel 2 XL and iOS devices - iPhone 5-X, iPad and iPad Pro. 

The issues faced were the compatibility of the website with Safari and Internet Explorer on the desktop, specifically Windows 10. The dropdown menu with the checkbox filters on the index page was also not aligned properly with screen widths less than 1920px – which was mentioned previously in the ‘Features Left to Implement’ section of this documentation.

## Deployment
This site is hosted using Heroku, deployed directly from the master branch and Github. The deployed site will update automatically upon new commits to the master branch.

To run locally, you can clone this repository directly into the editor of your choice by pasting heroku git:clone -a lyfartshackdb into your terminal.

## Credits
### Media
I do not own any of the artwork photos and their details and description of the artstyles in the ‘Information’ page were taken from various websites
Description of artstyles: 
https://www.widewalls.ch/what-is-abstract-art-informel/
https://magazine.artland.com/art-movements-and-styles/
https://steinhardt.nyu.edu/programs/art-education/art-education-definitions
https://ourpastimes.com/what-is-figurative-art-12213514.html
https://www.tate.org.uk/art/art-terms/m/minimalism
http://www.mynewsdesk.com/sg/artyii/news/nanyang-style-singapore-s-pioneer-art-movement-25399
Icons are from the Font Awesome CDN https://fontawesome.com/v4.7.0/icons/
### Acknowledgements
Template and tutorial of MongoDB, Flask and Jinja provided by the lecturer
https://github.com/kunxin-chor/mongo-sample-batch-3
Searchbox with dropdown menu was found through this demo here
https://www.jquery-az.com/bootstrap-search-box-with-additional-filters-2-demos/
Webkit searchbox cancel button credits to Stackoverflow user Tuc3k
https://stackoverflow.com/questions/35583503/input-type-search-no-longer-shows-cancel-button-x-under-ios

**This is for educational use.**
