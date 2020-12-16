from django.contrib import admin

# Register your models here.

from .models import Game, User, Question, Node

admin.site.register(Game)
admin.site.register(User)
admin.site.register(Question)
admin.site.register(Node)