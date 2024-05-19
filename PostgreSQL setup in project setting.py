PostgreSQL Setup in Project

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'student_db',  #database name in PGAdmin application
        'USER': 'postgres',
        'PASSWORD': '12345',
        'HOST': '127.0.0.1',          #localhost where django runserver
        'PORT': '5432',
    }
}