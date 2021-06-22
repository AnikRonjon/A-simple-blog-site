from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm


class UserDashboardForm(UserChangeForm):
    date_joined = forms.DateTimeField(disabled=True)
    last_login = forms.DateTimeField(disabled=True)
    username = forms.CharField(disabled=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'date_joined', 'last_login']