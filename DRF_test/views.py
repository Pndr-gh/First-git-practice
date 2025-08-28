from django.shortcuts import render
from rest_framework.generics import GenericAPIView, ListCreateAPIView

from .serializers import UserSerializer
from django.contrib.auth.models import User

class UserAPIView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

