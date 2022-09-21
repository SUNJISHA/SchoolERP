from django.urls import path
from . import views

urlpatterns=[
    path('studhome',views.student_studhome),
    path('profile',views.student_profile),
    path('changepassword',views.student_changepassword),
]