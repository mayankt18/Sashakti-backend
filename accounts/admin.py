from django.contrib import admin

# Register your models here.
from .models import Employer, Course, Skill, Job, User

admin.site.register(Employer)
admin.site.register(Course)
admin.site.register(Skill)
admin.site.register(Job)
admin.site.register(User)
