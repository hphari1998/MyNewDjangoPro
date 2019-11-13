from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from signup.forms import SignUpForm


def signupForm(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        passwordConfirm = request.POST.get('passwordConfirm')

        obj = User()
        obj.username = username
        obj.first_name = firstname
        obj.last_name = lastname
        obj.email = email
        obj.password = password
        obj.check_password = passwordConfirm
        obj.save()
         
        return redirect('/signin/')
    
    return render(request, 'cred/signup.html')
