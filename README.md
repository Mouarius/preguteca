# Videoteca Sondeo (ex Preguteca)

This is the code for the website [Videoteca Sondeo](https://www.videotecasondeo.com) an online ressource for discussing about videos of society topics.

## Technical description
This website is divided into :
- a frontend made with VueJS.
- a backend as a Django server that is serving the index page containing the frontend code, and endpoints for a REST API using Django REST Framework for interacting with the database.

## Developping locally
To run the website on your local machine, you will need to install the required dependencies in the frontend, and in the backend.

### Frontend (`preguteca_frontend`)
#### Installation
Run `npm install` to install the dependencies

#### Running the development server
Run `npm run dev` to run the local `vite` development server locally.

### Backend (`preguteca_backend`)
#### Setup the python virtual environment
1. Setup a *python virtual enviromnent* with the method of your choice (ex: https://docs.python.org/3/library/venv.html)
2. Install the required dependencies with `pip install -r requirements.txt`
3. Initialize the database with `python manage.py migrate`
4. Be sure to load a dump of the production site if you want some data to start with
5. Run the django server with `python manage.py runserver`
