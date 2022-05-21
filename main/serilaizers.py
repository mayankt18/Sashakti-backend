from rest_framework import serializers
from accounts.models import Course

class CourseSerializer(serializers.ModelSerializer):


    def create(self, validated_data):
        return Course.objects.create(**validated_data)

    class Meta:
        model = Course
        fields = '__all__'
