from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Candidate, Employer, Tutor


UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    def create(self, validated_data):

        user = UserModel.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
        )

        return user

    class Meta:
        model = UserModel
        
        fields = ( "id", "username", "password", )


class EmployerSerializer(serializers.ModelSerializer):

    user = serializers.PrimaryKeyRelatedField(
        default=serializers.CurrentUserDefault(),
        queryset=UserModel.objects.all(),
    )

    class Meta:
        model = Employer
        fields = ['id', 'name', 'user', 'email', 'phone', 'address', 'city', 'state', 'zipcode', 'country', 
        'company_name', 'company_description', 'company_website', 'company_logo']


class CandidateSerializer(serializers.ModelSerializer):

    user = serializers.PrimaryKeyRelatedField(
        default=serializers.CurrentUserDefault(),
        queryset=UserModel.objects.all(),
    )

    class Meta:
        model = Candidate
        fields = ['id', 'name', 'user', 'email', 'phone', 'address', 'city', 'state', 'zipcode', 'country', 
        'qualification', 'skill']


class TutorSerializer(serializers.ModelSerializer):

    user = serializers.PrimaryKeyRelatedField(
        default=serializers.CurrentUserDefault(),
        queryset=UserModel.objects.all(),
    )

    class Meta:
        model = Tutor
        fields = ['id', 'name', 'user', 'email', 'company', 'qualifications', 'about', 'image']
