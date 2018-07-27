'''
Views.py - Django Standart File Views

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
from django.template import loader
from django.http import HttpResponse
from django import views
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.forms import modelformset_factory
from django.views.generic import (CreateView, DeleteView, ListView, FormView, UpdateView)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import  ClassRoom, School, Course, CustomUser, Take
from .forms import SignUpForm, SchoolCreateForm, ClassRoomCreateForm, CourseForm, GiveGradesForm

# Create your views here.
def index(request):
    '''
    Home Page
    '''
    print('index called')
    return render(request, 'index.html')

class SignUp(CreateView):
    '''
    New User Signup
    '''
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        role = form.cleaned_data['role']
        obj.user_type = role
        form.save()
        return super().form_valid(form)

class UserListView(LoginRequiredMixin, ListView):
    '''
    Users List
    '''
    model = CustomUser
    ordering = ('name', )
    context_object_name = 'Users'
    template_name = 'userslist.html'
    raise_exception = True

    def test_func(self):
        print('UserListview UserType:{0}'.format(self.request.user.user_type)) 
        return True

    def get_queryset(self):
        return CustomUser.objects.order_by('user_type')

class SchoolListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    '''
    School List
    '''
    model = School
    ordering = ('name', )
    context_object_name = 'Schools'
    template_name = 'Manager/schoollist.html'
    raise_exception = True

    def test_func(self):
        print('SchoolListview UserType:{0}'.format(self.request.user.user_type))
        if self.request.user.user_type != 3:
            print('User type mismatch, test_func denied')
            return False
        return True

    def get_queryset(self):
        return School.objects.order_by('name')

class SchoolCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    '''
    School Create
    '''
    model = School
    form_class = SchoolCreateForm
    template_name = 'Manager/school.html'
    success_url = reverse_lazy('schoollist')
    raise_exception = True

    def test_func(self):
        print('SchoolCreatView UserType:{0}'.format(self.request.user.user_type))
        if self.request.user.user_type != 3:
            print('User type mismatch, test_func denied')
            return False
        return True

    def get_login_url(self):
        if not self.request.user.is_authenticated:
            print('not authenticated')
            return super(SchoolCreateView, self).get_login_url()
        return ''      

    def get_context_data(self, **kwargs):
        context = super(SchoolCreateView, self).get_context_data(**kwargs)
        context['title'] = "Add School"
        return context  

class SchoolUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    '''
    Update School
    '''
    model = School
    form_class = SchoolCreateForm
    template_name = 'Manager/school.html'
    success_url = reverse_lazy('schoollist')
    raise_exception = True

    def test_func(self):
        print('SchoolUpdateView UserType:{0}'.format(self.request.user.user_type))
        if self.request.user.user_type != 3:
            print('User type mismatch, test_func denied')
            return False
        return True
    
    def get_login_url(self):
        if not self.request.user.is_authenticated:
            print('not authenticated')
            return super(SchoolUpdateView, self).get_login_url()
        return ''      

    def get_context_data(self, **kwargs):
        context = super(SchoolUpdateView, self).get_context_data(**kwargs)
        context['title'] = "Modify School"
        return context  

class SchoolDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    '''
    Delete School
    '''
    model = School
    fields = ('id', 'name', 'city')
    context_object_name = 'school'
    success_url = reverse_lazy('schoollist')
    template_name = 'Manager/deleteschool.html'
    raise_exception = True

    def test_func(self):
        print('SchoolDeleteView UserType:{0}'.format(self.request.user.user_type))
        if self.request.user.user_type != 3:
            print('User type mismatch, test_func denied')
            return False
        return True

class ClassRoomListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    '''
    Class Room List
    '''
    model = ClassRoom
    ordering = ('name', )
    context_object_name = 'ClassRooms'
    template_name = 'Manager/classroomlist.html'
    raise_exception = True

    def test_func(self):
        print('ClassRoomListView UserType:{0}'.format(self.request.user.user_type))
        if self.request.user.user_type != 3:
            print('User type mismatch, test_func denied')
            return False
        return True

    def get_queryset(self):
        return ClassRoom.objects.order_by('school')

class ClassRoomCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    '''
    Create Class Room
    '''
    model = ClassRoom
    form_class = ClassRoomCreateForm
    success_url = reverse_lazy('classroomlist')
    template_name = 'Manager/classroom.html'
    raise_exception = True

    def test_func(self):
        print('ClassRoomCreateView UserType:{0}'.format(self.request.user.user_type))
        if self.request.user.user_type != 3:
            print('User type mismatch, test_func denied')
            return False
        return True

    def get_login_url(self):
        if not self.request.user.is_authenticated:
            print('not authenticated')
            return super(ClassRoomCreateView, self).get_login_url()
        return ''

    def get_context_data(self, **kwargs):
        context = super(ClassRoomCreateView, self).get_context_data(**kwargs)
        context['title'] = "Add Class Room"
        return context  

class ClassRoomUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    '''
    Create Class Room
    '''
    model = ClassRoom
    form_class = ClassRoomCreateForm
    success_url = reverse_lazy('classroomlist')
    template_name = 'Manager/classroom.html'
    raise_exception = True

    def test_func(self):
        print('ClassRoomCreateView UserType:{0}'.format(self.request.user.user_type))
        if self.request.user.user_type != 3:
            print('User type mismatch, test_func denied')
            return False
        return True

    def get_login_url(self):
        if not self.request.user.is_authenticated:
            print('not authenticated')
            return super(ClassRoomUpdateView, self).get_login_url()
        return ''
    
    def get_context_data(self, **kwargs):
        context = super(ClassRoomUpdateView, self).get_context_data(**kwargs)
        context['title'] = "Modify Class Room"
        return context  

class ClassRoomDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    '''
    Delete Class Room
    '''
    model = ClassRoom
    fields = ('name', 'school')
    context_object_name = 'classRoom'
    success_url = reverse_lazy('classroomlist')
    template_name = 'Manager/deleteclassroom.html'
    raise_exception = True

    def test_func(self):
        print('ClassRoomDeleteview UserType:{0}'.format(self.request.user.user_type))
        if self.request.user.user_type != 3:
            print('User type mismatch, test_func denied')
            return False
        return True

    #def delete(self, request, *args, **kwargs):
        #return super().delete(request, *args, **kwargs)

class StudentListview(LoginRequiredMixin, UserPassesTestMixin, ListView):
    '''
    Students List
    '''
    model = Take    
    context_object_name = 'Students'
    template_name = 'studentlist.html'
    raise_exception = True

    def test_func(self):
        return True
    
    def get_queryset(self):
        course = Course.objects.get(id=self.kwargs['pk'])        
        return Take.objects.filter(course_id=course.id).order_by('student__first_name')
    
    def get_context_data(self, **kwargs):
        context = super(StudentListview, self).get_context_data(**kwargs)
        course = Course.objects.get(id=self.kwargs['pk'])     
        context['title'] = "Student List for {0}".format(course.name)
        return context 

class CourseListview(LoginRequiredMixin, UserPassesTestMixin, ListView):
    '''
    Course List
    '''
    model = Course
    ordering = ('name', )
    context_object_name = 'Courses'
    template_name = 'courselist.html'
    raise_exception = True

    def test_func(self):
        print('CourseListview UserType:{0}'.format(self.request.user.user_type))
        return True

    def get_queryset(self):
        print('CourseListview UserType:{0}'.format(self.request.user.user_type))
        if self.request.user.user_type == 1:            
            return Course.objects.exclude(id__in=Take.objects.filter(student=self.request.user).values_list('course_id', flat=True)).order_by('name').order_by('name')
        else:            
            return Course.objects.all().order_by('name')
        #return Course.objects.order_by('name').filter(self.request.user.id!=lecturer_id)        

class CourseCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    '''
    Course Create
    '''
    form_class = CourseForm    
    template_name = 'Lecturer/course.html'
    success_url = reverse_lazy('courselist')
    raise_exception = True
    model = Course

    def test_func(self):
        print('CourseCreateView UserType:{0}'.format(self.request.user.user_type))
        if self.request.user.user_type != 2:
            print('User type mismatch, test_func denied')
            return False
        return True

    def get_login_url(self):
        if not self.request.user.is_authenticated:
            print('not authenticated')
            return super(CourseCreateView, self).get_login_url()
        return ''
    
    def form_valid(self, form):
        print('Form Valid')
        obj = form.save(commit=False)              
        print(self.request.user)
        obj.lecturer = self.request.user
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        print('Form Invalid')
        print(form.errors)
        return super().form_invalid(form)   
        #return self.render_to_response(self.get_context_data(form=form))        
    
    def get_context_data(self, **kwargs):
        context = super(CourseCreateView, self).get_context_data(**kwargs)
        context['title'] = "Create Course"   
        context['crlist'] = ClassRoom.objects.all()        
        return context  

class CourseUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    '''
    Course Create
    '''
    form_class = CourseForm       
    template_name = 'Lecturer/course.html'
    success_url = reverse_lazy('courselist')
    raise_exception = True
    model = Course

    def test_func(self):
        print('CourseUpdateView UserType:{0}'.format(self.request.user.user_type))
        if self.request.user.user_type != 2:
            print('User type mismatch, test_func denied')
            return False
        course = Course.objects.get(id=self.kwargs['pk'])
        #course = Course.objects.get(id='pk')
        if self.request.user.id != course.lecturer.id:
            print('Owner mismatch, test_func denied')
            return False
        return True

    def get_login_url(self):
        if not self.request.user.is_authenticated:
            print('not authenticated')
            return super(CourseUpdateView, self).get_login_url()
        return ''
    
    def form_valid(self, form):
        print('Form Valid')
        obj = form.save(commit=False)              
        print(self.request.user)
        obj.lecturer = self.request.user
        form.save()
        return super().form_valid(form)  

    def form_invalid(self, form):
        print('Form Invalid')
        print(form.errors)          
        return self.render_to_response(self.get_context_data(form=form))          

    def get_context_data(self, **kwargs):
        context = super(CourseUpdateView, self).get_context_data(**kwargs)
        context['title'] = "Update Course"
        context['crlist'] = ClassRoom.objects.all()   
        return context 

class CourseDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    '''
    Delete Course
    '''
    model = Course
    fields = ('id', 'name', )
    context_object_name = 'course'
    success_url = reverse_lazy('courselist')
    template_name = 'Lecturer/deletecourse.html'
    raise_exception = True

    def test_func(self):
        print('CourseDeleteView UserType:{0}'.format(self.request.user.user_type))
        if self.request.user.user_type != 2:
            print('User type mismatch, test_func denied')
            return False
        course = Course.objects.get(id=self.kwargs['pk'])
        if self.request.user.id != course.lecturer.id:
            print('Owner mismatch, test_func denied')
            return False
        return True

@login_required(login_url='login')
def Enroll(request, pk):
    '''
    Student Enroll
    '''
    if request.user.user_type != 1:
        return HttpResponseRedirect('/')

    print("Student {0} Enroll Course with id {1} ".format(request.user.id, pk))
    Take.objects.get_or_create(student=request.user, course=Course.objects.get(id=pk))
    return HttpResponseRedirect('/courselist')

class TakenCoursesListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    '''
    Taken Course List
    '''
    model = Take
    ordering = ('name', )
    context_object_name = 'TakenCourses'
    template_name = 'Student/takencourses.html'
    raise_exception = True

    def test_func(self):
        print('TakenCoursesListView UserType:{0}'.format(self.request.user.user_type))
        if self.request.user.user_type != 1:
            print('User type mismatch, test_func denied')         
            return False    
        return True

    def get_queryset(self):
        return Take.objects.filter(student=self.request.user) \
            .select_related().order_by('course__name')


class GiveGradesView(LoginRequiredMixin, UserPassesTestMixin, views.View):
    template = 'Lecturer/givegrades.html'
    raise_exception = True

    def test_func(self):
        print('GiveGradesView UserType:{0}'.format(self.request.user.user_type)) 
        course = Course.objects.get(id=self.kwargs['pk'])
        if self.request.user.id != course.lecturer.id:
            print('Owner mismatch, test_func denied')
            return False      
        return True

    def get(self, request, pk):       
        takeFormSet = modelformset_factory(Take, extra=0, form=GiveGradesForm, fields=('id', 'studentName', 'grade'))
        formSet = takeFormSet(queryset=Take.objects.filter(course_id=pk))                
        course = Course.objects.get(id=pk)
        #print('Take objects total:{0}'.format(Take.objects.count()))
        context = {'formset': formSet, 'crs': course }
        template = loader.get_template(self.template)

        return HttpResponse(template.render(context, request))

    def post(self, request, pk):
        takeFormSet = modelformset_factory(Take, extra=0, form=GiveGradesForm, fields=('id', 'grade'))
        formSet = takeFormSet(request.POST)        
        
        context = {'formset': formSet}
        template = loader.get_template(self.template)
        if formSet.is_valid():                 
            for form in formSet.forms:
                if form.is_valid():
                    form.save()

            #takens = formSet.save(commit=False)
            #for take in takens:
                #take.save()

            return HttpResponseRedirect('/courselist/')
        else:
            print(formSet.non_form_errors())
            print(formSet.errors)
            
        
        return HttpResponse(template.render(context, request))