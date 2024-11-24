from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from .models import User
from django.contrib.auth.hashers import make_password, check_password

@api_view(['POST'])
def register(request):
    username = request.data['username']
    password = request.data['password']
    hashed_password = make_password(password)

    if User.objects.filter(username=username).exists():
        return Response({"error": "Username already exists"}, status=HTTP_400_BAD_REQUEST)

    user = User(username=username, master_password_hash=hashed_password)
    user.save()
    return Response({"message": "User registered successfully"}, status=HTTP_201_CREATED)

@api_view(['POST'])
def login(request):
    username = request.data['username']
    password = request.data['password']
    try:
        user = User.objects.get(username=username)
        if check_password(password, user.master_password_hash):
            return Response({"message": "Login successful"}, status=HTTP_201_CREATED)
        else:
            return Response({"error": "Invalid credentials"}, status=HTTP_400_BAD_REQUEST)
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=HTTP_400_BAD_REQUEST)

