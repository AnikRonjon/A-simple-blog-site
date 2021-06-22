from django.contrib.auth import login, logout
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.list import ListView
from django.contrib.auth.forms import authenticate, AuthenticationForm, UserCreationForm
from django.contrib import messages
from .models import Post


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


def user_dashboard_view(request):
    if request.user.is_authenticated:
        return render(request, 'classapp/dashboard.html')
    else:
        return redirect('/login/')


def user_registration_view(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                new_user = authenticate(username=form.cleaned_data['username'],
                                        password=form.cleaned_data['password1'])
                login(request, new_user)
                messages.add_message(request, messages.SUCCESS, f'Hurray! now {request.user} is registered user.')
                return redirect('/dashboard/')
        else:
            form = UserCreationForm()
        return render(request, 'classapp/registration.html', {'form': form})
    else:
        return redirect('/login/')


def user_login_view(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=username, password=password)
                login(request, user)
                messages.add_message(request, messages.SUCCESS, f'{request.user} login successfully')
                return redirect('/dashboard/')
        else:
            form = AuthenticationForm()
        return render(request, 'classapp/login.html', {'form': form})
    else:
        return redirect('/login/')


def user_logout_view(request):
    if request.user.is_authenticated:
        messages.add_message(request, messages.SUCCESS, f'{request.user} logout successfully. Continue with login.')
        logout(request)
        return redirect('/login/')
    else:
        return redirect('/login')



