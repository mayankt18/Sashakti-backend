from django.urls import path
from . import views

urlpatterns = [
    path('courses/getcourses',views.ListCoursesView.as_view(), name = 'getcourses'),
    path('courses/createcourse',views.CreateCoursesView.as_view(), name='createcourse'),
    path('courses/coursesByTutor',views.ListCoursesByTutorView.as_view(), name='coursesByTutor'),
    path('courses/getcoursedetail/<id>',views.CourseDetailView.as_view(),name='getcoursedetail'),


    path("skills/getskills",views.ListSkillsView.as_view(),name="getskills"),
    path('skills/createskill',views.CreateSkillsView.as_view(), name='createskill'),
    path('skills/skillsByCandidate',views.ListSkillsByCandididate.as_view(), name='skillsByCandidate'),


    path('jobs/getjobs',views.ListJobsView.as_view(), name = 'getjobs'),
    path('jobs/createjob',views.CreateJobsView.as_view(), name='createjob'),
    path('jobs/jobsByEmployer',views.ListJobsByEmployerView.as_view(), name='jobsByEmployer'),
    path('jobs/getjobdetail/<id>',views.JobDetailView.as_view(),name='getjobdetail'),


    path('candidate/candidatejob',views.CandidateJobsView.as_view(), name='candidatejobs'),
    path('candidate/candidatecourse', views.CandidateCourseView.as_view(), name='candidatecourse'),

    path('search/jobs/<query>', views.SearchJobView.as_view(), name='searchjob'),
    path('search/course/<query>', views.SearchCourseView.as_view(), name='searchcourse'),

    path('top/courses/<count>', views.TopCoursesView.as_view(), name='topcourses'),
    path('top/jobs/<count>', views.TopJobsView.as_view(), name='topjobs'),
]