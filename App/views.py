from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from datetime import datetime
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm

from .decorators import user_log_in_required,only_for_unauthenticated
# Create your views here.

def coverPage(request):
    return render(request, "obscura/cover.html", {})

def galleryPage(request):
    return render(request, "obscura/gallery.html", {})

@only_for_unauthenticated
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username').strip()
        pwd = request.POST.get('pwd').strip()

        obj = User.objects.filter(name=username,pwd=pwd)
        print(obj[0])
        if(len(obj)==1):
            request.session['user'] = username
            return redirect('Home')
        else:
            messages.error(request,'Invalid login credential! Please enter a valid username and password')
            return render(request, "obscura/login.html", {})
    else:
        return render(request,"obscura/login.html",{})


    #msg = request.session.get('msg', '')
    #if( msg ) : del(request.session['msg'])
    #return render(request, "obscura/login.html", {'msg':msg})

@user_log_in_required
def logout(request):
    if 'user' in request.session:
        request.session.pop('user')
    return redirect('Login')


@only_for_unauthenticated
def registerPage(request):

    form = CreateUserForm()
    context = {'form' : form }

    if request.method=='GET':
        return render(request, "obscura/register.html", context)
    else:
        name = request.POST.get('name').strip()
        pwd = request.POST.get('pwd').strip()
        obj = User.objects.filter(name=name)
        if len(obj)==1:
            messages.error(request,'User already exists!')
            return render(request, "obscura/register.html", {'msg':'User already exists. Please choose another username.'})
        else:
            obj = User.objects.create(name=name, pwd=pwd)
            obj.save()
            createObjects(obj)
            messages.success(request,"Registered Successfully!")
            #print('user created!')
            return redirect('Login')

@user_log_in_required
def homePage(request):
    return render(request, "obscura/home.html", {})

@user_log_in_required

def question(request):
    return render(request, "obscura/question.html", {})

@user_log_in_required 
def brickbreaker(request):
    if request.method == 'GET':
        obj = lboardGames(1)
        return render(request,"obscura/games/brickbreaker.html", {'lb':obj})

@user_log_in_required
def flappy(request):
    if request.method == 'GET':
        obj = lboardGames(2)
        return render(request, "obscura/games/flappy.html",{'lb':obj})

@user_log_in_required
def pianotiles(request):
    if request.method == 'GET':
        obj = lboardGames(3)
        return render(request, "obscura/games/pianotiles.html", {'lb':obj})

@user_log_in_required
def twotho(request):
    if request.method == 'GET':
        obj = lboardGames(4)
        return render(request, "obscura/games/twotho.html", {'lb':obj})

@user_log_in_required
def typing(request):
    if request.method == 'GET':
        obj = lboardGames(5)
        print(obj)
        return render(request, "obscura/games/typing.html", {'lb':obj})


#Extra functions
def createObjects(obj):
    for i in range(1, 6):
        objGame = Game.objects.create(name=obj, gameId=i)
        objGame.save()
    for i in range(1,7):
        objGame = Node.objects.create(name=obj, nodeNumber=i)
        objGame.save()


def registrationPage(request):
    form = CreateUserForm()
    context = {'form' : form }

    if request.method=='POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registered Successfully!")
            print('user created!')
            return redirect('Login')

    context = {'form' : form }
    return render(request, "obscura/register.html", context)
        


#leaderboard for games
def lboardGames(id):
    obj = Game.objects.filter(gameId=id).order_by('-score','name')[:6]
    return obj
