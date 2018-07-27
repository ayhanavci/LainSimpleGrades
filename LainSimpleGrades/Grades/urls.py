'''
urls.py - Django Standart File Url Routing

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
from django.urls import path
from . import views

#Common
urlpatterns = [
    path('', views.index, name='index'),
    path('enroll/', views.Enroll, name='enroll'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('userslist/', views.UserListView.as_view(), name='userslist'),
    path('studentlist/<int:pk>', views.StudentListview.as_view(), name='studentlist')
]

#Managers
urlpatterns += [
    path('schoollist/', views.SchoolListView.as_view(), name='schoollist'),
    path('addschool/', views.SchoolCreateView.as_view(), name='addschool'),
    path('editschool/<int:pk>/', views.SchoolUpdateView.as_view(), name='editschool'),
    path('deleteschool/<int:pk>/delete/', views.SchoolDeleteView.as_view(), name='deleteschool'),
    path('addclassroom/', views.ClassRoomCreateView.as_view(), name='addclassroom'),
    path('classroomlist', views.ClassRoomListView.as_view(), name='classroomlist'),
    path('editclassroom/<int:pk>/', views.ClassRoomUpdateView.as_view(), name='editclassroom'),
    path('deleteclassroom/<int:pk>/delete/', views.ClassRoomDeleteView.as_view(), name='deleteclassroom'),
]

#Lecturers
urlpatterns += [
    path('courselist/', views.CourseListview.as_view(), name='courselist'),
    path('addcourse/', views.CourseCreateView.as_view(), name='addcourse'),
    path('editcourse/<int:pk>/', views.CourseUpdateView.as_view(), name='editcourse'),
    path('deletecourse/<int:pk>/delete/', views.CourseDeleteView.as_view(), name='deletecourse'),    
    path('givegrades/<int:pk>', views.GiveGradesView.as_view(), name='givegrades'),    
]

#Students
urlpatterns += [
    path('enroll/<int:pk>/', views.Enroll, name='enroll'),
    path('takencourses/', views.TakenCoursesListView.as_view(), name='takencourses'),
]