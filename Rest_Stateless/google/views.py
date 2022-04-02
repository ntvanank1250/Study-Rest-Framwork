from operator import imod
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from rest_framework.utils import json
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content ={'message': 'Hello, World!'}
        return Response(content)