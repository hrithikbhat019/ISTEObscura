from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from datetime import datetime
# Create your views here.

def loginPage(request):
    msg = request.session.get('msg', '')
    if( msg ) : del(request.session['msg'])
    return render(request, "login.html", {'msg':msg})

def registerPage(request):
    if request.method=='GET':
        return render(request, "register.html", {})
    else:
        name = request.POST.get('name').strip()
        pwd = request.POST.get('pwd').strip()
        obj = User.objects.filter(name=name,pwd=pwd)
        if len(obj)==1:
            messages.error(request,'User already exists!')
            request.session['msg'] = 'User already exists!'
            return redirect('/login/')
        else:
            obj = User.objects.create(name=name, pwd=pwd)
            obj.save()
            return redirect('/login/')


def homePage(request):
    return render(request, "home.html", {})

def question(request):
    return render(request, "question.html", {})

def brickbreaker(request):
    return render(request,"games/brickbreaker.html", {})

def flappy(request):
    return render(request, "games/flappy.html",{})

def pianotiles(request):
    return render(request, "games/pianotiles.html", {})

def twotho(request):
    return render(request, "games/twotho.html", {})

def typing(request):
    return render(request, "games/typing.html", {})