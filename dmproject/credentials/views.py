from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    return render(request,"login.html")
def register(request):
    if request.method == 'POST':
        username1 = request.POST['username']
        first_name1 = request.POST['first_name']
        last_name1 = request.POST['last_name']
        email1 = request.POST['email']
        password1 = request.POST['password']
        cpassword1 = request.POST['password1']
        if password1 == cpassword1:
            if User.objects.filter(username=username1).exists():
                messages.info(request,"Username Taken")
                return redirect('register')
            elif User.objects.filter(email=email1).exists():
                messages.info(request, "Email Taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username1,first_name=first_name1,last_name=last_name1,email=email1,password=password1)
                user.save();
                return redirect('login')
        else:
            messages.info(request,"password not matching")
            return redirect('register')
        return redirect('/')
    return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
