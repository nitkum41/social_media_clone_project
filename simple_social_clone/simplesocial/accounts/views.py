from django.shortcuts import render
from django.urls import reverse_lazy #if somene is logged in where they should go
from django.views.generic import CreateView

from . import forms

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login') #where to go but only after successful submission
    template_name = 'accounts/signup.html'



# Create your views here.
