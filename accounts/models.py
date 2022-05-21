from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User
# Create your models here.


class Employer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=10, validators=[MinLengthValidator(10)], blank=True, null=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    zipcode = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    company_name = models.CharField(max_length=100, null=True, blank=True)
    company_description = models.CharField(max_length=100, null=True, blank=True)
    company_website = models.CharField(max_length=100, null=True, blank=True)
    company_logo = models.CharField(max_length=100, null=True, blank=True)


class Tutor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    company = models.CharField(max_length=100, null=True, blank=True)
    qualifications = models.CharField(max_length=200, blank=True, null=True)
    about = models.TextField(max_length=512, blank=True, null=True)
    image = models.URLField(blank=True, null=True)


class Course(models.Model):
    name = models.CharField(max_length=100)
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    description = models.CharField(max_length=100, null=True, blank=True)
    price = models.FloatField(default=0)
    duration = models.IntegerField(default=0)
    image = models.CharField(max_length=100, null=True, blank=True)
    organization = models.CharField(max_length=100, null=True, blank=True)


class Skill(models.Model):
    skill_name = models.CharField(max_length=100)
    skill_description = models.CharField(max_length=100)
    skill_created_at = models.DateTimeField(auto_now_add=True)
    skill_updated_at = models.DateTimeField(auto_now=True)


class Job(models.Model):
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=100)
    job_description = models.CharField(max_length=100)
    job_location = models.CharField(max_length=100, null=True, blank=True)
    job_type = models.CharField(max_length=100, null=True, blank=True)
    job_salary = models.CharField(max_length=100, null=True, blank=True)
    job_experience = models.CharField(max_length=100, null=True, blank=True)
    job_skills = models.ForeignKey(Skill, on_delete=models.CASCADE)
    job_status = models.CharField(max_length=100, null=True, blank=True)
    job_created_at = models.DateTimeField(auto_now_add=True)
    job_updated_at = models.DateTimeField(auto_now=True)


class Candidate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=10, validators=[MinLengthValidator(10)], blank=True, null=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    zipcode = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    qualification = models.CharField(max_length=100, null=True, blank=True)
    skill = models.ManyToManyField(Skill, blank=True)

