from rest_framework.generics import ListAPIView,CreateAPIView
from rest_framework.permissions import IsAuthenticated

from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_201_CREATED
)
from rest_framework.response import Response

from accounts.models import Course
from .serilaizers import CourseSerializer
# Create your views here.

class ListCoursesView(ListAPIView) :
    queryset = Course.objects.all()

    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]

class CreateCoursesView(CreateAPIView):
    queryset = Course.objects.all()

    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]

    def post(self,request,*args,**kwargs):
        user = request.user
        if not True :
            return Response({'error':'Only Employers can create courses'},status=HTTP_400_BAD_REQUEST)
        serializer = CourseSerializer(data = request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data,status=HTTP_201_CREATED)
        return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)






