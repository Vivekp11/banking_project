from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth

# Create your views here.
def home(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        user = User.objects.create_user(username, password1, password2)
        user.save()

        return redirect('signin')
    return render(request, 'register.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        my_user = auth.authenticate(username=username, password=password)

        if my_user is not None:
            auth.login(request, my_user)
            return redirect('form')
        else:
            messages.info(request, "invalid user")
            return redirect('log')

    return render(request, 'log.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def click(request):
    return render(request, 'click.html')

def form(request):
    return render(request, 'form.html')

def message(request):
    return render(request, 'message.html')