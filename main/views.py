import imp
from django.shortcuts import render
from httplib2 import Response

from rest_framework.generics import ListAPIView,CreateAPIView
from rest_framework.permissions import IsAuthenticated

from accounts.models import Course
from .serilaizers import CourseSerializer
# Create your views here.

class ListCoursesView(ListAPIView) :
    queryset = Course.objects.all()

    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]



