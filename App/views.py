from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from datetime import datetime
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from random import randint
from django.http import JsonResponse,HttpResponse



from .decorators import user_log_in_required,only_for_unauthenticated
# Create your views here.
@only_for_unauthenticated
def initialPage(request):
    return render(request, "obscura/initial.html", {})
    
def instructionPage(request):
    return render(request, "obscura/instructions.html", {})

@only_for_unauthenticated
def coverPage(request):
    return render(request, "obscura/cover.html", {})

@user_log_in_required
def galleryPage(request):
    context = {
        'obj':''
    }
    name = request.session['user']
    objUser = User.objects.get(name = name)
    objNode = Node.objects.filter(name = objUser)
    for i in objNode:
        nodeName = 'node' + str(i.nodeNumber)
        if i.score > 0:
            context[nodeName] = '1'
    return render(request, "obscura/gallery.html", context)

@user_log_in_required
def galleryView(request,nodeNumber):
    nodeNumber = int(nodeNumber)
    if nodeNumber == 1:
        return render(request, 'obscura/galleryFolder/mandp.html')
    elif nodeNumber == 2:
        return render(request, 'obscura/galleryFolder/nand.html')
    elif nodeNumber == 3:
        return render(request, 'obscura/galleryFolder/fnh.html')
    elif nodeNumber == 4:
        return render(request, 'obscura/galleryFolder/hcc.html')
    elif nodeNumber == 5:
        return render(request, 'obscura/galleryFolder/sja.html')
    elif nodeNumber == 6:
        return render(request, 'obscura/galleryFolder/lhcc.html')
    elif nodeNumber == 7:
        return render(request, 'obscura/galleryFolder/sprtcmp.html')
    elif nodeNumber == 8:
        return render(request, 'obscura/galleryFolder/beach.html')
    elif nodeNumber == 9:
        return render(request, 'obscura/galleryFolder/sac.html')
    elif nodeNumber == 10:
        return render(request, 'obscura/galleryFolder/lhcb.html')
    elif nodeNumber == 11:
        return render(request, 'obscura/galleryFolder/library.html')

@only_for_unauthenticated
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username').strip()
        pwd = request.POST.get('pwd').strip()

        obj = User.objects.filter(name=username,pwd=pwd)
        #print(obj[0])
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
    nameSession = request.session['user']
    obj = User.objects.get(name = nameSession)
    objNodes = Node.objects.filter(name = obj)
    listVisited = {}
    listScore = {}
    for i in objNodes:
        if i.visited:
            listVisited[int(i.nodeNumber)] = True 
        if i.score > 0:
            listScore[int(i.nodeNumber)] = True
    return render(request, "obscura/home.html", {'obj':obj, 'node':listVisited, 'score':listScore})


def leaderboardPage(request):
    obj = lboard()
    return render(request, "obscura/leaderboard.html", {'lb':obj})

@user_log_in_required
def question(request, diff, node):
    context = {
        'question':'This is a question with options',
        'op1':'',
        'op2':'',
        'op3':'',
        'op4':''
    }
    nameUser = request.session['user']
    objUser = User.objects.get(name = nameUser)
    objNode = Node.objects.get(name = objUser, nodeNumber = str(node))
    objNode.visited = True
    objNode.save()
    if request.method == 'GET':
        questions = Question.objects.filter(difficulty = str(diff))
        numberOfQuestions = questions.count()
        randomIndex = randint(1,numberOfQuestions)
        context['question'] = questions[randomIndex - 1].quest
        context['op1'] = questions[randomIndex - 1].op1
        context['op2'] = questions[randomIndex - 1].op2
        context['op3'] = questions[randomIndex - 1].op3
        context['op4'] = questions[randomIndex - 1].op4
        request.session['question'] = context['question']
        request.session['ans'] = questions[randomIndex - 1].ans
        #print(request.session['question'],request.session['ans'])
    else:
        #print(request.session['question'],request.session['ans'])
        context['question'] = request.session['question']
        context['answered'] = 1
        ansAct = request.session['ans']
        ansPost = request.POST.get('answer').strip()
        print(ansAct,ansPost)
        request.session.pop('question')
        request.session.pop('ans')
        if int(ansAct) == int(ansPost) and objNode.score == 0:
            context['msg'] = 'You have answered the question correctly! Go back to Home to solve more!'
            flag = 0
            if objNode.score == 0:
                flag = 1
            if int(diff) == 1:
                objNode.score = 50
            elif int(diff) == 2:
                objNode.score = 100
            elif int(diff) == 3:
                objNode.score = 150
            objNode.save()
            objUser.score += objNode.score
            objUser.save()
        else:
            context['msg'] = 'You have answered the question wrong! Come back later and try again!' 



    return render(request, "obscura/question.html", context)

@user_log_in_required 
def brickbreaker(request):
    objLBoard = lboardGames(1)
    if request.method == 'GET':
        return render(request,"obscura/games/br2.html", {'lb':objLBoard})
    elif request.method == 'POST':
        #+2 for each brick
        scorePost = int(request.POST.get('score').strip())
        name = request.session['user']
        objUser = User.objects.get(name = name)
        obj = Game.objects.get(name = objUser, gameId = 1)
        if obj.score < scorePost:
            objUser.score += scorePost - obj.score
            objUser.save()
            obj.score = scorePost
            obj.save()
            return HttpResponse(status = 201)
        else:
            return HttpResponse(status = 200)

@user_log_in_required
def flappy(request):
    #3x score
    if request.method == 'GET':
        obj = lboardGames(2)
        return render(request, "obscura/games/flappy.html",{'lb':obj})

    elif request.method == 'POST':
        score = int(request.POST.get('score').strip())
        normalised_score = 3*score
        #print(score)
        #print(request.POST)
        name = request.session['user']
        objUser = User.objects.get(name = name)
        obj = Game.objects.get(name = objUser, gameId = 2)
        if obj.score < normalised_score:
            objUser.score += normalised_score - obj.score
            objUser.save()
            obj.score = normalised_score
            obj.save()

        obj = lboardGames(2)
        return HttpResponse(status =201)


@user_log_in_required
def pianotiles(request):
    # score as is
    if request.method == 'GET':
        obj = lboardGames(3)
        return render(request, "obscura/games/pianotiles.html", {'lb':obj})
    elif request.method == 'POST':
        scorePost = int(request.POST.get('score').strip())
        #print(score)
        #print(request.POST)
        name = request.session['user']
        objUser = User.objects.get(name = name)
        obj = Game.objects.get(name = objUser, gameId = 3)
        if obj.score < scorePost:
            objUser.score += scorePost - obj.score
            objUser.save()
            obj.score = scorePost
            obj.save()
            return HttpResponse(status = 201)

@user_log_in_required
def twotho(request):
    if request.method == 'GET':
        obj = lboardGames(4)
        return render(request, "obscura/games/twotho.html", {'lb':obj})
    elif request.method == 'POST':
        score = int(request.POST.get('score').strip())
        #print(score)
        #print(request.POST)
        name = request.session['user']
        objUser = User.objects.get(name = name)
        obj = Game.objects.get(name = objUser, gameId = 4)
        if obj.score < scorePost:
            objUser.score += scorePost - obj.score
            objUser.save()
            obj.score = scorePost
            obj.save()
            return HttpResponse(status = 201)

@user_log_in_required
def typing(request):
    #score as is
    if request.method == 'GET':
        obj = lboardGames(5)
        print(obj)
        return render(request, "obscura/games/typing.html", {'lb':obj})
    elif request.method == 'POST':
        scorePost = int(request.POST.get('score').strip())
        #print(score)
        #print(request.POST)
        name = request.session['user']
        objUser = User.objects.get(name = name)
        obj = Game.objects.get(name = objUser, gameId = 5)
        if obj.score < scorePost:
            objUser.score += scorePost - obj.score
            objUser.save()
            obj.score = scorePost
            obj.save()
            return HttpResponse(status = 201)

def baseView(request):
    return render(request,'base.html')

#Extra functions
def createObjects(obj):
    for i in range(1, 6):
        objGame = Game.objects.create(name=obj, gameId=i)
        objGame.save()
    for i in range(1,16):
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

#leaderboard for entire users
def lboard():
    obj = User.objects.order_by('-score', 'name')[:6]
    return obj
