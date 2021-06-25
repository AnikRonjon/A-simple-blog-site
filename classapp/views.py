from django.contrib.auth import login, logout, update_session_auth_hash
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView
from django.views.generic.list import ListView
from django.contrib.auth.forms import PasswordChangeForm, authenticate, AuthenticationForm, UserCreationForm
from django.contrib import messages
from .models import Post
from .forms import UserDashboardForm


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
        if request.method == "POST":
            form = UserDashboardForm(data=request.POST, instance=request.user)
            if form.is_valid():
                form.save()
        else:
            form = UserDashboardForm(instance=request.user)

        if request.method == "POST":
            p_form = PasswordChangeForm(data=request.POST, user=request.user)
            if p_form.is_valid():
                p_form.save()
                update_session_auth_hash(request, p_form.user)
                return redirect('/dashboard/')
        else:
            p_form = PasswordChangeForm(user=request.user)
        return render(request, 'classapp/dashboard.html', {'form': form, 'p_form': p_form})
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


class PostView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_list'] = Post.objects.all()
        return context
