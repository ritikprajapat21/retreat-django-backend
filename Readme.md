# Wellness Retreat Backend
A basic backend service to manage retreat data for a fictional wellness retreat webpage. This service provide an API to fetch retreat information and allow users to book a retreat.

# Tech Stack
- Django
- Djano Rest Framework
- Django Environ
- Django Taggit

# Local setup
Installing the dependencies:
```
pip install -r requirement.txt
```
Before running, run following:
```
python manage.py makemigrations
python manage.py migrate
```

Run the app
```
python manage.py runserver
```