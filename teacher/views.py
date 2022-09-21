from django.shortcuts import render

# Create your views here.


def teacher_home(request):
    return render(request,'teacher/home.html')

def teacher_addstudent(request):
    return render(request,'teacher/addstudent.html') 

def teacher_viewstudent(request):
    return render(request,'teacher/viewstudent.html')  

def teacher_changepassword(request):
    return render(request,'teacher/changepassword.html')        