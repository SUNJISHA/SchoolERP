from django.urls import path
from . import views

urlpatterns=[
    path('home',views.teacher_home),
    path('addstudent',views.teacher_addstudent),
    path('viewstudent',views.teacher_viewstudent),
    path('changepassword',views.teacher_changepassword),
    
]