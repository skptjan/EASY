from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
import os
from .forms import SignUpForm
from .models import *
# Create your views here.


def indexView(request):
    data = {
        'page': 'Frontend/home.html',
    }

    return render(request, 'Frontend/index.html', data)


def loginView(request):
    if request.method == 'POST' and 'login' in request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/home')
            else:
                data = {
                    'page': 'registration/login.html',
                    'error': 'User account not activated',
                }
                return render(request, 'Frontend/index.html', data)
        else:
            data = {
                'page': 'registration/login.html',
                'error': 'Incorrect password and/or username',
            }
            return render(request, 'Frontend/index.html', data)

    data = {
        'page': 'registration/login.html',
        'error': '',
    }

    return render(request, 'Frontend/index.html', data)


def registerView(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            newUser = form.save()
            profile = Profile.objects.create(user=newUser, plan=request.POST['plan'])
            profile.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()

    data = {
        'page': 'registration/register.html',
        'form': form,
    }

    return render(request, 'Frontend/index.html', data)


def logoutView(request):
    logout(request)
    return redirect('Home')


def dashboardView(request):
    data = {
        'page': 'Frontend/dashboard.html',
    }

    return render(request, 'Frontend/index.html', data)


def profileView(request):
    data = {
        'page': 'Frontend/profile.html',
    }

    return render(request, 'Frontend/index.html', data)


def aboutUsView(request):
    data = {
        'page': 'Frontend/about-us.html',
    }

    return render(request, 'Frontend/index.html', data)


def contactView(request):
    data = {
        'page': 'Frontend/contact.html',
    }

    return render(request, 'Frontend/index.html', data)


def plansView(request):
    # if request.method == 'POST' and 'plan' in request.POST and request.user.is_authenticated:
    #     user = User.objects.get(username=request.user.username)
    #     form = PlansForm(request.POST)
    #     if form.is_valid():
    #         user.save()
    #         form.save()
    #         return redirect('/dashboard')
    # else:
    #     form = PlansForm()
    #     data = {
    #         'page': 'Frontend/plans.html',
    #         'form': form,
    #         'error': 'Not logged in',
    #     }
    #
    #     return render(request, 'Frontend/index.html', data)
    plan = Plan.objects.all()

    data = {
        'page': 'Frontend/plans.html',
        'plan': plan,
        # 'form': form,
    }

    return render(request, 'Frontend/index.html', data)


def handler404(request, *args, **argv):
    if request.get_full_path != f"{os.path}":
        data = {
            'page': 'Frontend/404.html',
        }
        return render(request, 'Frontend/index.html', data)
