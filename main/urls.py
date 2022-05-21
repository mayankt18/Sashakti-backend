from django.urls import path
from . import views

urlpatterns = [
    path('',views.Course),
    path('courses/getcourses',views.ListCoursesView.as_view(), name = 'getcourses')

]