from django.shortcuts import render
from projects.models import Experience, AboutMe, Skills, EducationDetails


def project_index(request):
    projectExp = Experience.objects.all()
    aboutMe = AboutMe.objects.all()
    skills = Skills.objects.all()
    educations = EducationDetails.objects.all()
    context = {
        'projectExp': projectExp,
        'aboutMe': aboutMe,
        'skills': skills,
        'educations': educations,
    }
    return render(request, 'index.html', context)
