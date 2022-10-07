from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=100)
    about = models.TextField(max_length=2000)
    embed_link = models.CharField(max_length=200)
    video_link = models.CharField(max_length=200)
    github_repo = models.CharField(max_length=500)
    languages = models.JSONField()

    def __str__(self):
        return self.name

class Blog(models.Model):
    name = models.CharField(max_length=100)
    about = models.TextField(max_length=2000)
    picture_link = models.CharField(max_length=200)
    blog_link = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

class Certificate(models.Model):
    name = models.CharField(max_length=100)
    picture_link = models.CharField(max_length=200)
    validation = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    about = models.TextField(max_length=2000)
    book_cover = models.CharField(max_length=200)
    link = models.CharField(max_length=1000)

    def __str__(self):
        return self.title

class QAndA(models.Model):
    name = models.CharField(max_length=50, default="Anonymous")
    question = models.TextField(max_length=1000)
    answer = models.TextField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return f"{self.name}: {self.question}"