from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout

# Create your views here.
from django.contrib.auth import authenticate,login
def login_attempt(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.filter(email = email).first()
        if not user:
            message = {"error":"User Doesn't Exists"}
            context = message
            return render(request, 'auth/login.html', context)
        user = authenticate(username=email, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            message = {"error":"Invalid Credentials"}
            context = message
            return render(request, 'auth/login.html', context)
    return render(request, 'auth/login.html')

def register_attempt(request):
    context = {
        "title":"Register Page"
    }
    if request.method == "POST":
        f_name = request.POST.get('firstName')
        l_name = request.POST.get('lastName')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.filter(email = email).first()

        if user:
            message = {"error":"User Already Exists"}
            context = message
            return render(request, 'auth/register.html', context)
        user = User(first_name=f_name, last_name=l_name, email = email, username=email)
        user.set_password(password)
        user.save()

    return render(request, 'auth/register.html')

def logout_attempt(request):
    logout(request)
    return redirect('/')