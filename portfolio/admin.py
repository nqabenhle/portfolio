from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Project)
admin.site.register(Certificate)
admin.site.register(Book)
admin.site.register(Blog)
admin.site.register(QAndA)
admin.site.register(Skill)