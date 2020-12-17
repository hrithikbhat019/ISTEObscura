from django.contrib import admin
# Register your models here.
from .models import Game, User, Question, Node

class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'pwd', 'score')

class GameAdmin(admin.ModelAdmin):
    list_display = ('name', 'gameId', 'score')
    list_filter = ('gameId',)
    
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('quest', 'ans', 'difficulty')
    
class NodeAdmin(admin.ModelAdmin):
    list_display = ('name', 'nodeNumber', 'score', 'visited')

admin.site.register(User, UserAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Node, NodeAdmin)