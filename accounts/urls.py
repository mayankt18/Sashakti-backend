from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('accounts/register', views.CreateUserView.as_view(), name='register'),
    path('accounts/login', views.login, name='login'),
]