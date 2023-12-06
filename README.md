# Simple Flask App

Simple Flask app created for Python Programming Final Project. This project is a fully functional website for an imaginary cafe that I created. It has a home page with custom copy and a custom logo. All credit goes to the owners of the photographs I pulled from various sources. The website also has a menu page that connects to a database I created to display the contents of the menu.

I want to emphasize this is **NOT** a real cafe, but I *would* like to one day open up this cafe so there are a *LOT* of fine details and my own ideas throughout this website, so **please respect that** and *don't steal my idea(s)* haha.

## README Contents:
1. How to run
2. Things to Note

## How to Run:
I have on here the entire directory for my virtual environment that I used throughout my development process for grading purposes, but if you are wanting to reproduce that environment I also have a requirements.txt file that you can use to install all the dependencies for this project directly into your own virtual environment. 
**NOTE:** this requirements file will *ONLY* work if you are using pip (as opposed to Conda). Once you have a virtual environment directory simply make sure you are inside it and use: 
`pip install -r requirements.txt` to install all dependencies.

Additionally, make sure you specify the path to that file if it is not in your working directory.

Once you have the dependencies installed you should be able to run the project using `python -m flask run` with no errors! :smile:

## Things to Note:
### Database
My database can be found in the instance directory of this project. It is titled shop.db 
There are two python files that can be discarded but I have kept them here just so you can see how I 1. created the database and 2. updated it. 
db_create.py was used to create the database and update_db.py was used to update the database as needed. 
But since my project uses shop.db you do not really need these files.

### Repository will NOT remain public
Once I have received my final grade for this class, I will be making this repo private. This is because like I mentioned before, I do want to open up this cafe eventually and I do not want anybody to take the concept or even the menu (I worked hard to come up with the menu) and compete with my future business. Thank you for your understanding!
