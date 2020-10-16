from django.shortcuts import render
from rest_framework import viewsets
from blog.models import Post
from users.models import Profile
from django.contrib.auth.models import User
from .serializers import UserSerializer, PostSerializer, ProfileSerializer


# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer