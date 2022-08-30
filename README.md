# Hasker
poor man`s stackoverflow

# online version
http://gctmlp.ru/

# About

This is educational project, which functional is similar to stackoverflow.com
Technology stack is:
  - Nginx
  - uWSGI
  - Django
  - Vue.js
  - MySQL
  - Smarty templates

# How to deploy

1. Clone the repository
```
git clone https://github.com/GCTMLP/otus_hasker.git
```
```
cd otus-hasker
```

2. Install requirements
```
pip3 install -r requirements.txt
```

3. Create database named "hasker"
```
mysql -u "username" -p
create database hasker;
```

4. Write your mysql configuration at "config/settings.py"
examlpe:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'hasker',
        'USER': 'username',
        'PASSWORD': 'password',
        'HOST': 'yourhost' (ex: localhost),
        'PORT': 'yourport',
    }
}
```

5. Apply migrations
```
python3 manage.py makemigration
python3 manage.py migrate
```

6. Add your server name at "config/settings.py"
example
```
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '[::1]', 'gctmlp.ru']
```
7. Set up nginx
example configuration at "/etc/nginx/sites-enabled/hasker"
```
```
