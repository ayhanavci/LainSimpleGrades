'''
forms.py - Django Standart File Forms

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
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, School, ClassRoom, Course, Take

class SignUpForm(UserCreationForm):
    '''
    Form to signup a new user
    '''
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')    
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Type a valid email address.')
      
    CHOICES=[('1','I am a Student'), 
         ('2','I am a Lecturer'), 
         ('3','I am a School Manager')]
    role = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), help_text='Please Select Role:', initial='1')

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')       

class SchoolCreateForm(forms.ModelForm):
    '''
    Create new school form
    '''
    class Meta:
        model = School
        fields = ['name', 'city', ]

        
class ClassRoomCreateForm(forms.ModelForm):
    '''
    Create new class room form
    '''
    class Meta:
        model = ClassRoom
        fields = ['name', 'school']              
    
class CourseForm(forms.ModelForm):
    '''
    Create new course form
    '''    
    school = forms.ModelChoiceField(queryset=School.objects.all(), empty_label=None)

    class Meta:
        model = Course        
        fields = ['code', 'name', 'school', 'classRoom',]       
    
    def __init__(self, *args, **kwargs):        
        super().__init__(*args, **kwargs)        
        self.fields['classRoom'].queryset = ClassRoom.objects.none()                                         
      
        if self.instance.pk: #Update
            school_id = self.instance.classRoom.school_id
            self.initial['school'] = self.instance.classRoom.school            
            self.fields['classRoom'].queryset = ClassRoom.objects.all()
            self.initial['classRoom'] = self.instance.classRoom                                   
        else: #Create                        
            if School.objects.all().count():
                firstSchool = School.objects.all().first()                
                self.fields['classRoom'].queryset = ClassRoom.objects.all()
                
class GiveGradesForm(forms.ModelForm):
    '''
    Lecturer gives grades to student
    '''    
    studentName = forms.CharField(help_text='Student Name:', max_length=100)    

    class Meta:
        model = Take
        fields = [            
            'id', 'grade', 'studentName',
        ]        
    
    def __init__(self, *args, **kwargs):
        super(GiveGradesForm, self).__init__(*args, **kwargs)
        if self.instance:                                                     
            if hasattr(self.instance, 'student'):                
                self.initial['studentName'] = self.instance.student.first_name + ' ' + self.instance.student.last_name  
                self.fields['studentName'].widget.attrs['readonly'] = True
          
