from django.urls import path

from . import views

app_name = "portfolio"

urlpatterns = [
    path("", views.index, name="index"),
    path("question/add", views.add_question, name="question"),
    path("about", views.about, name="about"),
    path("projects", views.projects, name="projects"),
    path("blogs", views.blogs, name="blogs")
]