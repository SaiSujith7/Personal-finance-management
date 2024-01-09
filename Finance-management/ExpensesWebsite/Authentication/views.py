from django.shortcuts import render, redirect
from django.views import View
import json
from django.http import JsonResponse
from django.contrib.auth.models import User
import json
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.urls import reverse
from django.contrib import auth

# Create your views here.

class EmailValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        email = data['email']
        if not validate_email(email):
            return JsonResponse({'email_error': 'Email is invalid'}, status=400)
        if User.objects.filter(email=email).exists():
            return JsonResponse({'email_error': 'sorry email in use,choose another one '}, status=409)
        return JsonResponse({'email_valid': True})

class UsernameValidationView(View):
    def post(self,request):
        data=json.loads(request.body)
        username=data['username']

        if not str(username).isalnum():
            return JsonResponse({'username_error':'username should only alphanumeric characters'},status=400)
        if User.objects.filter(username=username).exists():
            return JsonResponse({'username_error':'sorry username in user,choose another one'},status=409)
        return JsonResponse({'username_valid': True})
    
def RegistrationView(request):
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']

        data= User.objects.create_user(username=username,email=email,password=password)
        data.save()
        return redirect('login')
    return render(request,'authentication/register.html')


def LoginView(request):
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']

        user=auth.authenticate(username=username,email=email,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('Expenses')
    return render(request,'authentication/login.html')

def LogoutView(request):
    auth.logout(request)
    return redirect('login')