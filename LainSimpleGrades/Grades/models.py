'''
models.py - Django Standart File Models

This file is part of Lain Simple Grades.

Lain Simple Grades is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Lain Simple Grades is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Lain Simple Grades.  If not, see <https://www.gnu.org/licenses/>.
'''

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator

class CustomUser(AbstractUser):
    '''
    Custom User Model for authentication
    '''
    USER_TYPE_CHOICES = (
        (0, 'Admin'),
        (1, 'Student'),
        (2, 'Lecturer'),   
        (3, 'Manager'),
    )

    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, default=0)
    def __str__(self):
        return self.username

class School(models.Model):
    '''
    School model
    '''
    name = models.CharField(max_length=50, help_text="Enter School Name")
    
    CITY_CHOICES = (        
        (1, 'Istanbul'),
        (2, 'London'),   
        (3, 'Tokyo'),
        (4, 'New York'),
        (5, 'Berlin'),
        (6, 'Moscow'),
    )

    city = models.PositiveSmallIntegerField(choices=CITY_CHOICES, default=1)
    
    def __str__(self):
        return self.name

class ClassRoom(models.Model):
    '''
    ClassRoom in school
    '''
    name = models.CharField(max_length=50, help_text="Enter Classroom Name")
    school = models.ForeignKey('School', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

class Course(models.Model):
    '''
    Course model
    '''
    name = models.CharField(max_length=50, help_text='Enter Course Name')
    code = models.CharField(max_length=10, help_text='Enter Course Code')    
    classRoom = models.ForeignKey('ClassRoom', on_delete=models.SET_NULL, null=True, help_text='Select Class Room')
    lecturer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    students = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='Students', help_text='Students')

    def __str__(self):
        return "{0} ({1})".format(self.name, self.code)


class Take(models.Model):
    '''
    Take model. Student grades.
    '''
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    grade = models.PositiveIntegerField(blank=True, null=True, help_text='Grade', 
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)])
    