from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from datetime import datetime
# Create your views here.

def coverPage(request):
    return render(request, "cover.html", {})

def galleryPage(request):
    return render(request, "gallery.html", {})

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
        obj = User.objects.filter(name=name)
        if len(obj)==1:
            messages.error(request,'User already exists!')
            return render(request, "register.html", {'msg':'User already exists. Please choose another username.'})
        else:
            obj = User.objects.create(name=name, pwd=pwd)
            obj.save()
            createObjects(obj)
            return redirect('/login/')

def homePage(request):
    return render(request, "home.html", {})


def question(request):
    return render(request, "question.html", {})

#Games 
def brickbreaker(request):
    if request.method == 'GET':
        obj = lboardGames(1)
        return render(request,"games/brickbreaker.html", {'lb':obj})

def flappy(request):
    if request.method == 'GET':
        obj = lboardGames(2)
        return render(request, "games/flappy.html",{'lb':obj})

def pianotiles(request):
    if request.method == 'GET':
        obj = lboardGames(3)
        return render(request, "games/pianotiles.html", {'lb':obj})

def twotho(request):
    if request.method == 'GET':
        obj = lboardGames(4)
        return render(request, "games/twotho.html", {'lb':obj})

def typing(request):
    if request.method == 'GET':
        obj = lboardGames(5)
        print(obj)
        return render(request, "games/typing.html", {'lb':obj})


#Extra functions
def createObjects(obj):
    for i in range(1, 6):
        objGame = Game.objects.create(name=obj, gameId=i)
        objGame.save()
    for i in range(1,7):
        objGame = Node.objects.create(name=obj, nodeNumber=i)
        objGame.save()


#leaderboard for games
def lboardGames(id):
    obj = Game.objects.filter(gameId=id).order_by('-score','name')[:6]
    return obj
