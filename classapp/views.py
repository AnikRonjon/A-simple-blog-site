from django.shortcuts import render, get_object_or_404
from .models import User, Post
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView


# Create your views here.
class PostListView(ListView):
    model = Post
    context_object_name = 'posts'


def PostDetailView(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                             published__year=year,
                             published__month=month,
                             published__day=day)

    return render(request, 'classapp/post_detail.html', {'post': post})
