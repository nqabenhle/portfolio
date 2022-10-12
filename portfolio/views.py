import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

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