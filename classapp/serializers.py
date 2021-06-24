from rest_framework import serializers
from django.contrib.auth.forms import UserCreationForm
from .forms import UserDashboardForm
from .models import Category, Post


class UserCreationFormSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserCreationForm
        fields = ('id', 'username', 'password1', 'password2')


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        depth = 1


class CategorySerializer(serializers.ModelSerializer):
    post_serializer = PostSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'post_serializer')



