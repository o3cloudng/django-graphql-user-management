# User Management with Django and GraphQL


## Create virtual environment
```
python3 -m virtualenv venv
```
### Run virtual environemnt
```
source venv/bin/activate
```
### Install Django
```
pip install django
```

### Install GraphQL (Graphene)
```
pip install graphene-django
```

### Create Django Project & App
```
django-admin startproject core .
django-admin startapp account

python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

