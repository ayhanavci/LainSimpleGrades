# Lain Simple Grades

Lain Simple Grades is a barebone demo web application that can be used as a starting point for a school grading system. Admins, School Management, Teachers and Students can log in to system and perform grade related tasks. It is developed as a personal reference project for core Django and Docker features. For more details visit the article on my web site: [Lain.run](https://lain.run/)

Project is a standard Django application with zero external dependencies. The only reference to outside world is Font Awesome icons url in ```/Grades/templates/base.html``` file for cosmetic purposes. Should work if you remove that too.

For my blog post visit [Web With Python](https://lain.run/projects/Web-With-Python/)

Live demo at: http://grades.lain.run/

## Classic Method

Steps:

1. Optional: Install [Virtualenv](https://virtualenv.pypa.io/en/stable/) if you would like to isolate your  development environment from your host OS and to happily sandbox with different versions.

2. Install [Python](https://www.python.org/downloads/) and [Django](https://docs.djangoproject.com/en/2.0/topics/install/) if you haven't already. (I used ```homebrew```). The project was working fine with Python 3.7 and Django 2.0 versions.

3. Install the Django supported database of your choice. [Here is a list](https://docs.djangoproject.com/en/2.0/ref/databases/)

4. Get the code, edit ```/school/settings.py```. 

    4.a. Set the database. There are three options that I put in there, Sqlite, Local Postgre, Docker Postgre all of which I have used during development. Just uncomment the connection of your choice and edit pthe arameters. You can naturally use [any Database supported by Django]((https://docs.djangoproject.com/en/2.0/ref/databases/))

    ```Python
        '''
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
            }
        }
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': 'GradeDemo',
                'USER': 'gradedemoadmin',
                'PASSWORD': 'gradedemoadmin',
                'HOST': '127.0.0.1',
                'PORT': '5432',
            }
        }
        '''

        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': 'lainsimplegrades',
                'USER': 'ayhanavci',
                'PASSWORD': 'demopass',
                'HOST': 'db',
                'PORT': 5432,
            }
        }
    ```

    For simplicity, I recommend using Sqlite. Just uncomment the top option and comment the other two.



    4.b. You may want to edit the following parameters in ```/school/settings.py``` for production deployment.

    ```Python
    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = 's$0m8kpg7(syqnff9kwdc39w48_4ba__$c!p5_$(b()@2ys*g5'

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = True
    ```

5. cd to project root and run bash commands to create database using python (or use ```python3``` depending on your installation)

```bash
python manage.py makemigrations Grades
python manage.py migrate
python manage.py runserver
```

That's it. The application should work on http://127.0.0.1:8001/. If you would like to add an administrator account, run ```python manage.py createsuperuser``` before ```runserver``` but after ```migrate```, and follow instructions.

(You can change the port like this: ```python manage.py runserver 7000```)

## Installation With Docker

1. Download and extract zip from [here](https://github.com/ayhanavci/LainSimpleGrades/archive/master.zip) or from Bash

```bash
git clone https://github.com/ayhanavci/LainSimpleGrades.git
```

2. Enter directory and docker-compose up

```bash
cd LainSimpleGrades
docker-compose up
```

That's it. This command does all of the following in order;

Everything below 4 happens inside docker containers, so nothing gets installed on your host machine. Everything is isolated.

1. Downloads Official Python 3.7 Docker Image
2. Downloads Official Postgre Sql Docker Image
3. Creates docker images on your host (Python, Postgre and lainsimplegrades)
4. Creates docker containers from images
5. Binds the containers
6. Runs Postgre SQL
7. Waits for Postgres to be up and running, and then creates database and tables and hosts the web application.
8. Runs the web server inside lainsimplegrades container on port 8000 and binds it to your host's port 8001

The application should work at http://127.0.0.1:8001/. 

Before docker-compose;

* You may want to change settings in ```/school/settings.py``` as described above.
* If you change database settings in ```/school/settings.py```, you have to edit ```docker-compose.yml``` to match the values.
* If you want to change the port, edit ```docker-compose.yml```.

## Licence
Copyright © 2018 Ayhan Avcı - [Lain.run](https://lain.run/)

[GNU General Public License](https://www.gnu.org/licenses/#GPL)
