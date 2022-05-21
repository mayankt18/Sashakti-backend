from rest_framework import serializers
from accounts.models import Course, Job, Skill

class CourseSerializer(serializers.ModelSerializer):


    def create(self, validated_data):
        return Course.objects.create(**validated_data)

    class Meta:
        model = Course
        fields = '__all__'


class SkillSerializer(serializers.ModelSerializer):


    def create(self, validated_data):
        return Skill.objects.create(**validated_data)

    class Meta:
        model = Skill
        fields = '__all__'


class JobSerializer(serializers.ModelSerializer):


    def create(self, validated_data):
        return Job.objects.create(**validated_data)

    class Meta:
        model = Job
        fields = '__all__'
