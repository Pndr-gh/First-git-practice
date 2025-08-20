from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login as dj_login, logout as dj_logout

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
def home(request):
    if request.method == "GET":
        return render(request, 'home.html', {})
    
    elif request.method == 'POST':
        user_choice = request.POST.get('choice')

        if user_choice == 'login':
            return redirect('/login/')
        
        elif user_choice == 'logout':
            return redirect('/logout/')
        
        elif user_choice == 'signup':
            return redirect('/signup/')

        elif user_choice == 'all_users':
            return redirect('/allUsers/')

def show_users(request):
    if request.method == 'GET':
        if request.user.is_authenticated: 
            users = User.objects.all()
            return render(request, 'user_list.html', {'object_list': users})
        return render(request, 'button.html', {'context': 'not-loggedIn-m'})
    if request.method == 'POST':
        if request.POST.get('choice') == 'Home':
            return redirect('/')
def login(request):
    if request.method == "GET":
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})
    if request.method == 'POST':
        if request.POST.get('choice') == 'Home':
            return redirect('/')
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            dj_login(request, user)
            return render(request, 'button.html', {'context': 'login-m'})
        return render(request, 'login.html', {'form': form})
    return HttpResponse('method not allowed')
def signup(request):
    if request.method == "GET":
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})
    elif request.method == "POST":
        if request.POST.get('choice') == 'Home':
            return redirect('/')
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            return render(request, 'button.html', {'context': 'signup-m', 'username': username})
        else:

            return render(request, 'signup.html', {'form': form})
    return HttpResponse("mehtod not allowed")
def logout(request):
    user = request.user
    if request.method == 'GET':  
        if user:
            dj_logout(request)
            return render(request, 'button.html', {'context': 'logout-m', 'user': user})
        return HttpResponse("was not logged in anyway :)")
    
    elif request.method == "POST":
        if request.POST['choice'] == 'Home':
            return redirect('/')

    