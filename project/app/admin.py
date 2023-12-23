from django.contrib import admin

from .models import UserInfo, Skill, Project

# Register your models here.

admin.site.register(UserInfo)
admin.site.register(Skill)
admin.site.register(Project)
