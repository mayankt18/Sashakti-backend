from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model
from .serializers import CandidateSerializer, TutorSerializer, UserSerializer, EmployerSerializer
from .models import Candidate, Employer, Tutor

from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.oauth2.client import OAuth2Client


def home(request):
    return HttpResponse("Sashakti backend homepage....")


class CreateUserView(CreateAPIView):
    """
    POST accounts/register/
    """
    model = get_user_model()
    permission_classes = [AllowAny]
    serializer_class = UserSerializer


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    """
    POST accounts/login/
    """
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)


@csrf_exempt
@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def logout(request):
    """
    POST accounts/logout/
    """
    request.user.auth_token.delete()
    return Response(status=HTTP_200_OK)


@csrf_exempt
@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def get_user(request):
    """
    POST accounts/getuser/
    """
    return Response(UserSerializer(request.user).data)


@csrf_exempt
@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def update_employer_profile(request):
    """
    POST accounts/update_employer_profile/
    """
    context = {
        'request':request
    }
    try:
        employer = Employer.objects.get(user=request.user)
        serializer = EmployerSerializer(employer, data=request.data, context=context)
    except:
        serializer = EmployerSerializer(data=request.data, context=context)

    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=HTTP_200_OK)


@csrf_exempt
@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def update_candidate_profile(request):
    """
    POST accounts/update_candidate_profile/
    """
    context = {
        'request':request
    }
    try:
        employer = Candidate.objects.get(user=request.user)
        serializer = CandidateSerializer(employer, data=request.data, context=context)
    except:
        serializer = CandidateSerializer(data=request.data, context=context)

    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=HTTP_200_OK)


@csrf_exempt
@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def update_tutor_profile(request):
    """
    POST accounts/update_tutor_profile/
    """
    context = {
        'request':request
    }
    try:
        tutor = Tutor.objects.get(user=request.user)
        serializer = TutorSerializer(tutor, data=request.data, context=context)
    except:
        serializer = TutorSerializer(data=request.data, context=context)

    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=HTTP_200_OK)


@csrf_exempt
@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def get_user_profile(request):
    try:
        candidate = Candidate.objects.get(user=request.user)
        serializer = CandidateSerializer(candidate)
    except:
        try:
            employer = Employer.objects.get(user=request.user)
            serializer = EmployerSerializer(employer)
        except:
            try:
                tutor = Tutor.objects.get(user=request.user)
                serializer = TutorSerializer(tutor)
            except:
                return Response({"error":"user not found"},status=HTTP_404_NOT_FOUND)
    return Response(serializer.data,status=HTTP_200_OK)




class GoogleLogin(SocialLoginView):
    authentication_classes = [] # disable authentication
    adapter_class = GoogleOAuth2Adapter
    callback_url = "http://localhost:3000"
    client_class = OAuth2Client
