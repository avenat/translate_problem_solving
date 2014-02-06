## Interactive Python Book engine

How to install?

For local development, please add 'local.py' file to interactivepython/ directory with lines like this:

```
import os


BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite'),
    }
}
```

App apply migrations

```
python manage.py syncdb
python manage.py migrate
```

Run server

```
python manage.py runserver
```
