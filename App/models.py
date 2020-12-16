from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(default='',max_length=40)
    pwd = models.CharField(default='',max_length=100)
    score = models.IntegerField(default=0)

class Game(models.Model): #For any game, not implemented rn
    name = models.CharField(default='',max_length=40)
    score = models.IntegerField(default=0)

class Question(models.Model):
    quest = models.TextField()
    choice = [(1,'A'), (2, 'B'), (3, 'C'), (4, 'D')]
    ans = models.CharField(max_length = 2, choices = choice, default = 1)
    diff = [(1,'Easy'), (2,'Medium'), (3, 'Hard')]
    difficulty = models.CharField(max_length=2, choices = diff, default = 1)