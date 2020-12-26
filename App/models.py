from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(blank=False,null=False,max_length=40)
    pwd = models.CharField(blank=False,null=False,max_length=100)
    score = models.IntegerField(default=0)

class Game(models.Model): #For any game, not implemented rn
    name = models.ForeignKey(User, null = False, default = '',on_delete = models.SET_DEFAULT)
    score = models.IntegerField(default=0)
    choice = [('1','brickbreaker'), ('2', 'flappy'), ('3', 'pianotiles'), ('4', 'twotho'), ('5', 'typing')]
    gameId = models.CharField(max_length = 1, choices = choice, default = 1)

class Question(models.Model):
    quest = models.TextField()
    op1, op2, op3, op4 = models.TextField(default=''), models.TextField(default=''), models.TextField(default=''), models.TextField(default='')
    choice = [('1','1'), ('2', '2'), ('3', '3'), ('4', '4')]
    ans = models.CharField(max_length = 1, choices = choice, default = 1)
    diff = [('1','Easy'), ('2','Medium'), ('3', 'Hard')]
    difficulty = models.CharField(max_length=1, choices = diff, default = 1)
    

class Node(models.Model):
    name = models.ForeignKey(User, null = False, default = '',on_delete = models.SET_DEFAULT)
    choice = [('1','MbandP'),('2','Nan'),('3','FnH'),('4','HCC'),('5','SJA'),('6','LHCC')]
    for i in range(7,16):
        choice.append((str(i), (str(i))))
    nodeNumber = models.CharField(max_length=2, choices = choice, default = 1)
    score = models.IntegerField(default=0)
    visited = models.BooleanField(default=False)