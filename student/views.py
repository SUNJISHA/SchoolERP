from django.shortcuts import render

# Create your views here.


def student_studhome(request):
    return render(request,'student/studhome.html')

def student_profile(request):
    return render(request,'student/profile.html')

def student_changepassword(request):
    return render(request,'student/changepassword.html')    