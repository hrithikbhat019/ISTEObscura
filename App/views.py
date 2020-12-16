from django.shortcuts import render
# Create your views here.

def loginPage(request):
    return render(request, "login.html", {})

def registerPage(request):
    return render(request, "register.html", {})

def homePage(request):
    return render(request, "home.html", {})

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