import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core.mail import send_mail
from django import forms

from .models import *

# Create your views here.

def index(request):
    return render(request, "portfolio/index.html", {
        "skills": Skill.objects.all(),
        "projects": Project.objects.all()[:4],
        "blogs": Blog.objects.all()[:4],
        "certificates": Certificate.objects.all()[:3],
        "book": Book.objects.get()
    })

def add_question(request):
    data = json.loads(request.body)
    QAndA.objects.create(name=data.get("name"), question=data.get("question"))
    return JsonResponse({"message": "success"}, status=200)

def about(request):
    return render(request, "portfolio/about.html")

def projects(request):
    return render(request, "portfolio/projects.html", {
        "projects": Project.objects.all()
    })

def blogs(request):
    return render(request, "portfolio/blogs.html", {
        "blogs": Blog.objects.all()
    })

def certificates(request):
    return render(request, "portfolio/certificates.html", {
        "certificates": Certificate.objects.all()
    })

def skills(request):
    return render(request, "portfolio/skills.html", {
        "skills": Skill.objects.all()
    })

class HireForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Full Name"}))
    email = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Email"}))
    offer = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Job Offer"}))
    message = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control", "placeholder":"Job Description"}))
    

def hire(request):
    if request.method == "POST":
        data = json.loads(request.body)
        
        send_mail(
            "Job Offer",
            f"Hey Nqabenhle,\n{data.get('name')} sent you a job offer.\nJob Offer: {data.get('job_offer')}\nMessage: {data.get('message')}\nEmail: {data.get('email')}",
            "portfolio@livingdreams.com",
            ['nqabenhlemlaba22@gmail.com'],
            fail_silently=False,
        )

        return JsonResponse({"message": "success"}, status=200)

    else:
        return render(request, "portfolio/hire.html", {
            "form": HireForm()
        })