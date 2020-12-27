"""obscura URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from App.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',initialPage, name = 'Initial'),
    path('cover/', coverPage, name = 'Cover'),
    path('login/', loginPage, name = 'Login'),
    path('register/', registerPage, name = 'Register'),
    path('home/', homePage,name = 'Home'),
    path('brickbreaker/',brickbreaker ,name = 'BrickBreaker'),
    path('flappy/', flappy,name = 'Flappy'),
    path('pianotiles/', pianotiles, name = 'PianoTiles'),
    path('twotho/', twotho,name = 'TwoTho'),
    path('typing/', typing,name = 'Typing'),
    path('question/<diff>/<node>', question, name = 'Question'),
    path('gallery/', galleryPage, name = 'Gallery'),
    path('logout/',logout,name='Logout'),
    path('leaderboard/', leaderboardPage, name='LeaderBoard'),
    path('instructions/', instructionPage, name = 'Instructions'),
    path('galleryview/<nodeNumber>', galleryView, name='GalleryView'),
    path('base/',baseView,name='BaseView')
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
