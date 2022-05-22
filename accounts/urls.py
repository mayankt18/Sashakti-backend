from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('accounts/register', views.CreateUserView.as_view(), name='register'),
    path('accounts/login', views.login, name='login'),
    path('accounts/logout', views.logout, name="logout"),
    path('getuser', views.get_user, name="get_user"),
    path('getuserprofile',views.get_user_profile,name='get_user_profile'),
    path('update_employer_profile', views.update_employer_profile, name="update_employer_profile"),
    path('update_tutor_profile', views.update_tutor_profile, name="update_tutor_profile"),
    path('update_candidate_profile', views.update_candidate_profile, name="update_candidate_profile"),
]