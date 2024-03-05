python -m venv venv

.\venv\Scripts\activate

pip install django

pip freeze > requirements.txt

pip install -r requirements.txt

python -m django --version

create new django project

django-admin startproject projectname

pip install psycopg2

python3 manage.py startapp appname


## to run app

python manage.py runserver

.\venv\Scripts\activate

python manage.py makemigrations

python manage.py migrate