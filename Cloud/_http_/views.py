from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout

from django.http import HttpResponseRedirect
from django.urls import reverse

from django.db import IntegrityError
from .models import User, Train, TemperatureHumidity

from datetime import datetime


def index(request):
    context = {}
    if 'message' in request.session:
        context['message'] = request.session['message']
        del request.session['message']
    return render(request, '_http_/index.html', context=context)

def _login(request):
    context={}
    if request.method == 'POST':
        if 'email' and 'password' in request.POST:
            email, password = request.POST['email'], request.POST['password']
            u = authenticate(request, username=email, password=password)
            if u is not None:
                login(request, u)
                request.session['message'] = 'Successfully logged in'
                return HttpResponseRedirect(reverse('_http_:index'))
            else:
                context['message'] = 'Wrong credentials'
                return render(request, '_http_/login.html', context=context)
    elif request.method == 'GET':
        if request.user.is_authenticated:
            return render(request, '_http_/index.html', context=context)
        else:
            if 'message' in request.session:
                context['message'] = request.session['message']
                del request.session['message']
            return render(request, '_http_/login.html', context=context)
    
def _logout(request):
    context = {}
    if request.user.is_authenticated:
        logout(request)
        request.session['message'] = 'Successfully logged out'
        return HttpResponseRedirect(reverse('_http_:index'))
    else:
        return HttpResponseRedirect(reverse('_http_:login'))
    
def _register(request):
    context = {}
    if request.user.is_authenticated and request.user.role == 'Agent':
        if request.method == 'POST':
            if 'email' in request.POST:
                try:
                    u = User.objects.create_user(username=request.POST['email'], password='xxx')
                    u.save()
                except IntegrityError:
                    context['message'] = 'Credentials already in use'
                    return render(request, '_http_/register.html', context=context)
                request.session['message'] = 'Successfully registred'
                return HttpResponseRedirect(reverse('_http_:index'))
        elif request.method == 'GET':
            if 'message' in request.session:
                context['message'] = request.session['message']
                del request.session['message']
            return render(request, '_http_/register.html', context=context)
    else:
        context['message'] = 'Permission denied'
        return render(request, '_http_/permission-denied.html', context=context)

def train(request):
    context = {}
    if request.user.is_authenticated and request.user.role == 'Super':
        if 'message' in request.session:
            context['message'] = request.session['message']
            del request.session['message']
        if request.method == 'GET':
            if 'train' in request.GET:
                context['no_train'] = False
                context['temperatures'] = []
                context['humidities'] = []
                context['timestamps'] = []
                #data = list(TemperatureHumidity.objects.filter(train_id=request.GET['train']).order_by('timestamp'))
                data = list(TemperatureHumidity.objects.filter(train_id=request.GET['train']))
                for d in data[-10:]:
                    context['temperatures'].append(str(d.temperature))
                    context['humidities'].append(str(d.humidity))
                    context['timestamps'].append(d.timestamp)
            else:
                context['no_train'] = True
                context['trains'] = Train.objects.all()
            return render(request, '_http_/train.html', context=context)
    else:
        context['message'] = 'Permission denied'
        return render(request, '_http_/permission-denied.html', context=context)
    
def profile(request):
    context = {}
    print(request)
    if request.user.is_authenticated and request.user.role == 'Client':
        if 'message' in request.session:
            context['message'] = request.session['message']
            del request.session['message']
        if request.method == 'GET':
            return render(request, '_http_/profile.html', context=context)
    else:
        context['message'] = 'Permission denied'
        return render(request, '_http_/permission-denied.html', context=context)
