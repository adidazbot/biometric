# settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Change this to your desired database engine
        'NAME': 'company_x_db',               # Replace with your database name
        'USER': 'your_database_user',         # Replace with your database username
        'PASSWORD': 'your_database_password', # Replace with your database password
        'HOST': 'localhost',
        'PORT': '',
    }
}

