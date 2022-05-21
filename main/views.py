from rest_framework.generics import ListAPIView,CreateAPIView
from rest_framework.permissions import IsAuthenticated

from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_201_CREATED,
    HTTP_403_FORBIDDEN
)
from rest_framework.response import Response

from accounts.models import Course, Employer, Job, Skill
from .serilaizers import CourseSerializer, JobSerializer, SkillSerializer


class ListCoursesView(ListAPIView):
    queryset = Course.objects.all()

    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]

class CreateCoursesView(CreateAPIView):
    queryset = Course.objects.all()

    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]

    def post(self,request,*args,**kwargs):
        user = request.user
        if not True : #  TODO : Tutor Model
            return Response({'error':'Only Tutors can create courses'},status=HTTP_400_BAD_REQUEST)
        serializer = CourseSerializer(data = request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data,status=HTTP_201_CREATED)
        return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)








class ListSkillsView(ListAPIView):
    queryset = Skill.objects.all()

    serializer_class = SkillSerializer
    permission_classes = [IsAuthenticated]

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