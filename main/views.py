from accounts.serializers import EmployerSerializer
from rest_framework.generics import ListAPIView,CreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.shortcuts import get_object_or_404

from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_201_CREATED,
    HTTP_404_NOT_FOUND,
    HTTP_403_FORBIDDEN,
    HTTP_200_OK
)
from rest_framework.response import Response

from accounts.models import Course, Employer, Job, Skill, Candidate, Tutor
from .serilaizers import CourseSerializer, JobSerializer, SkillSerializer
from django.db.models import Q


class ListCoursesView(ListAPIView):
    queryset = Course.objects.all()

    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]


class ListCoursesByTutorView(ListAPIView):
    queryset = Course.objects.all()

    serializer_class = CourseSerializer
    permission_class = [IsAuthenticated]

    def get(self,request,*args,**kwargs):
        user = request.user

        try :
            tutor = Tutor.objects.get(user=user)
        except :
            return Response({'error':'Tutor not found'},status=HTTP_403_FORBIDDEN)

        serializer = CourseSerializer(Course.objects.filter(tutor=tutor),many=True)
        return Response(serializer.data,status=HTTP_200_OK)

class CreateCoursesView(CreateAPIView):
    queryset = Course.objects.all()

    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]

    def post(self,request,*args,**kwargs):
        user = request.user

        try:
            tutor = Tutor.objects.get(user=user)
        except :
            return Response({'error':'Tutor not found'},status=HTTP_403_FORBIDDEN)

        data = request.data.copy()

        data["tutor"] = int(tutor.id)

        serializer = CourseSerializer(data = data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data,status=HTTP_201_CREATED)
        return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)


class CourseDetailView(RetrieveAPIView):
    queryset = Course.objects.all()

    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "id"

    def get_object(self):
        queryset = self.get_queryset()
        filter = {}
        filter["id"] = self.kwargs["id"]

        obj = get_object_or_404(queryset, **filter)
        obj.views+=1
        obj.save()
        self.check_object_permissions(self.request, obj)
        return obj








class ListSkillsView(ListAPIView):
    queryset = Skill.objects.all()

    serializer_class = SkillSerializer
    permission_classes = [IsAuthenticated]

class ListSkillsByCandididate(ListAPIView):
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        try :
            candidate = Candidate.objects.get(user=user)
        except :
            return Job.objects.none()
        return candidate.jobs.all()


class CreateSkillsView(CreateAPIView):
    queryset = Skill.objects.all()

    serializer_class = SkillSerializer
    permission_classes = [IsAuthenticated]

    def post(self,request,*args,**kwargs):
        serializer = SkillSerializer(data = request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data,status=HTTP_201_CREATED)
        return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)








class ListJobsView(ListAPIView):
    queryset = Job.objects.all()

    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated]

class ListJobsByEmployerView(ListAPIView):
    queryset = Job.objects.all()

    serializer_class = JobSerializer
    permission_class = [IsAuthenticated]

    def get(self,request,*args,**kwargs):
        user = request.user

        try :
            employer = Employer.objects.get(user=user)
        except :
            return Response({'error':'Employer not found'},status=HTTP_403_FORBIDDEN)

        serializer = JobSerializer(Job.objects.filter(employer=employer),many=True)
        return Response(serializer.data,status=HTTP_200_OK)


class CreateJobsView(CreateAPIView):
    queryset = Job.objects.all()

    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated]

    def post(self,request,*args,**kwargs):
        user = request.user

        try :
            employer = Employer.objects.get(user=user)
        except :
            return Response({'error':'Employer not found'},status=HTTP_403_FORBIDDEN)

        data = request.data.copy()

        data["employer"] = int(employer.id)

        serializer = JobSerializer(data = data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data,status=HTTP_201_CREATED)
        return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)



class JobDetailView(RetrieveAPIView):
    queryset = Job.objects.all()

    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "id"

    def get_object(self):
        queryset = self.get_queryset()
        filter = {}
        filter["id"] = self.kwargs["id"]

        obj = get_object_or_404(queryset, **filter)
        obj.views+=1
        obj.save()
        self.check_object_permissions(self.request, obj)
        return obj

class CandidateJobsView(ListAPIView):
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        try :
            candidate = Candidate.objects.get(user=user)
        except :
            return Job.objects.none()
        return candidate.jobs.all()


class CandidateCourseView(ListAPIView):
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        try :
            candidate = Candidate.objects.get(user=user)
        except :
            return Course.objects.none()
        return candidate.courses.all()


class SearchJobView(ListAPIView):
    serializer_class = JobSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        jobs = Job.objects.filter(Q(job_title__icontains=self.kwargs['query']) | Q(job_description__icontains=self.kwargs['query']))
        return jobs

class SearchCourseView(ListAPIView):
    serializer_class = CourseSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        courses = Course.objects.filter(Q(name__icontains=self.kwargs['query']) | Q(description__icontains=self.kwargs['query']))
        return courses


class TopCoursesView(ListAPIView):
    serializer_class = CourseSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        courses = Course.objects.all().order_by('-views')[:int(self.kwargs['count'])]
        return courses

class TopJobsView(ListAPIView):
    serializer_class = JobSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        jobs = Job.objects.all().order_by('-views')[:int(self.kwargs['count'])]
        return jobs

