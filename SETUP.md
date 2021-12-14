Installation
To run on the PC must be installed: Python 3.9; Git;

Clone the repository

$ git clone https://github.com/IhorBereziak/park_cars.git
1) Setting up Django
At the root of the project, create a virtual environment and activate it

$ python -m venv “venv”
$ .\venv\Scripts\activate (for Linux: source ./venv/bin/activate)
All subsequent actions should be performed inside the virtual environment.
Install all required dependencies to work Django

$ pip install -r requirements.txt
In the core folder, copy the .env.example file to .env
Install all required migrations, make sure the file has been generated db.sqlite3

$ python manage.py makemigrations
$ python manage.py migrate

Run the project

$ python manage.py runserver

Before uploading to github
If you installed new dependencies in Django, then save them in requirenments.txt

$ pip freeze > requirements.txt