from urllib import response
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
import os
from .forms import SignUpForm, LampForm
from .models import *
# Create your views here.
from django.views.decorators.csrf import csrf_protect


def indexView(request):
    data = {
        'page': 'Frontend/home.html',
        'time': datetime.now()
    }

    return render(request, 'Frontend/index.html', data)

@csrf_protect
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
    # Lamps = Lamp.objects.all()
    # form = LampForm()
    #
    # if request.method == 'POST':
    #     form = LampForm(request.POST)
    #     if form.is_valid():
    #         newLamp = form.save(commit=False)
    #         newLamp.user = request.user
    #         newLamp.save()
    #     else:
    #         data = {
    #             'page': 'Frontend/dashboard.html',
    #             'Lamps': Lamps,
    #             'form': form,
    #             'error': 'Form is not valid',
    #         }
    #         return render(request, 'Frontend/index.html', data)
    #     return redirect('/dashboard')
    #
    # data = {
    #     'Lamps': Lamps,
    #     'form': form,
    #     'page': 'Frontend/dashboard.html',
    # }
    lamp_logs = LampLog.objects.filter(user=request.user).order_by('-time')

    data = {
        'LampLogs': lamp_logs,
        'page': 'Frontend/dashboard.html',
    }

    return render(request, 'Frontend/index.html', data)


def updateLamp(request, pk):
    lamp = Lamp.objects.get(id=pk)
    form = LampForm(instance=lamp)

    if request.method == 'POST':
        form = LampForm(request.POST, instance=lamp)
        if form.is_valid():
            form.save()
            return redirect('/dashboard')

    data = {
        'form': form,
        'page': 'Frontend/update-lamp.html',
    }

    return render(request, 'Frontend/index.html', data)


def deleteLamp(request, pk):
    lamp = Lamp.objects.get(id=pk)
    if request.method == 'POST':
        lamp.delete()
        return redirect('/dashboard')
    data = {
        'lamp': lamp,
        'page': 'Frontend/delete-lamp.html',
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


def makeMail(name, mail, sub, msg):
    data = {'name': name, 'mail': mail, 'sub': sub, 'msg': msg}
    MSG = '''
Webmail van:    {}
Mail adres :    {}
Message: 
{}
    '''.format(data['name'], data['mail'], data['msg'])
    contactForm = contact(name=name, email=mail, bericht=msg)
    contactForm.save()

    send_mail(data['sub'], MSG, 'webmail@', ['info@'],
              fail_silently=False, auth_user='webmail@', auth_password='')


def makeMailClient(mail):
    MSG = '''
Bedankt voor het invullen van ons contact formulier! Hierbij is bevestigd dat
wij uw mail ontvangen hebben. Wij zullen zo spoedig mogelijk contact met
u opnemen!
Vriendelijke groet,
(Naam)
'''
    send_mail('Bevestiging WebForm (Naam)', MSG, 'noreply@', [mail],
              fail_silently=False, auth_user='noreply@', auth_password='')

def contactView(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        bericht = request.POST.get('bericht')
        makeMail(name, email, 'Contactformulier (Naam)', bericht)
        makeMailClient(email)

        data = {
            'page': 'Frontend/contact-correct.html',
            'name': name,
        }
        return render(request, 'Frontend/index.html', data)

    else:

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
