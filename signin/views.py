from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect, HttpResponsePermanentRedirect

from signin.forms import SignInForm


def signinForm(request):
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
        login(request, user)
        return redirect('/articles/')

    return render(request, 'cred/signin.html')
