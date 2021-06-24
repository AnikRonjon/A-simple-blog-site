from django.shortcuts import render, redirect
from rest_framework.viewsets import ModelViewSet
from .models import Category, Post
from .forms import UserDashboardForm
from .serializers import CategorySerializer, PostSerializer, UserCreationFormSerializer


class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class PostModelViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
