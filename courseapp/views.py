from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import CreateUserForm


def login_user(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username or password is incorrect')

        context = {}
        return render(request, 'login.html', context)


def logout_user(request):
    logout(request)
    return redirect('login_user')


def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('login_user')

        context = {'form': form}
        return render(request, 'register.html', context)


def home(request):
    if request.user.is_authenticated:
        return redirect('intro')
    context = {}
    return render(request, 'home.html', context)


@login_required(login_url='login')
def intro(request):
    context = {}
    return render(request, 'intro.html', context)


@login_required(login_url='login')
def content(request):
    context = {}
    return render(request, 'content.html', context)


@login_required(login_url='login')
def quizzes(request):
    context = {}
    return render(request, 'quizzes.html', context)


@login_required(login_url='login')
def homework(request):
    context = {}
    return render(request, 'homework.html', context)

