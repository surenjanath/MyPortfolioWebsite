from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Contact, Resume_Experience, Resume_Education, Resume_Course, Resume_Skill, Resume_Achievement, Projects_item

# Create your views here.
def Home(request) :
    # return HttpResponse('Hello World')
    skills          = Resume_Skill.objects
    experience      = Resume_Experience.objects
    education       = Resume_Education.objects
    achievement     = Resume_Achievement.objects
    project         = Projects_item.objects
    context = {
               'Skills' : skills,
               'Experience'   : experience,
               'Education'    : education,
               'Achievements' : achievement,
               'Projects'      : project,
    }



    return render(request,'projects/home.html', context)
