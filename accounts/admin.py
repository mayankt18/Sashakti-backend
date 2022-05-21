from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Employer)
admin.site.register(Course)
admin.site.register(Skill)
admin.site.register(Job)
admin.site.register(Candidate)
admin.site.register(Tutor)
