#!/bin/sh

echo "Make Migrations"
python3 ./LainSimpleGrades/manage.py makemigrations Grades
echo "Migrate"
python3 ./LainSimpleGrades/manage.py migrate
echo "Run Server"
python3 ./LainSimpleGrades/manage.py runserver 0.0.0.0:8000