'''
admin.py - Django Standart File for Admin pages

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
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import School, Course, ClassRoom, CustomUser
from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


# Register your models here.

admin.site.register(School)
admin.site.register(Course)
admin.site.register(ClassRoom)


class CustomUserCreationForm(UserCreationForm):              
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')                

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser   
    ADDITIONAL_USER_FIELDS = (
        (None, {'fields': ('user_type',)}),
    )

    
    add_fieldsets = UserAdmin.add_fieldsets + ADDITIONAL_USER_FIELDS
    fieldsets = UserAdmin.fieldsets + ADDITIONAL_USER_FIELDS
    list_display = ['email', 'username', 'user_type']   

admin.site.register(CustomUser, CustomUserAdmin)
