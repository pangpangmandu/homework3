from django.shortcuts import render
from .models import Team
from django.shortcuts import redirect

def intro1(request):
    context = {

    }
    return render(request,'mta/intro1.html',context )


def intro2(request):
    context = {
        
    }
    return render(request,'mta/intro2.html',context )


def intro3(request):
    context = {
        
    }
    return render(request,'mta/intro3.html',context )


def new(request):
    return render(request, 'mta/new.html',{})

def main(request):

    if request.method == 'GET':
        context = {
            'teams': Team.objects.all()
        }
        return render(request, 'mta/main.html', context)
    elif request.method == 'POST':
        title = request.POST['title']
        Team.objects.create(title=title, score=0)
        return redirect('/main')

def delete(request, id):
    team = Team.objects.get(id=id)
    team.delete()
    return redirect('/main')


def insult(request):
    context = {
            'teams': Team.objects.all()
    }
    return render(request,'mta/insult.html',context)

def result(request):


    t = Team.objects.all()

    result = 0

    team = [] 
    teamg = request.GET['안경사자']
    teamb = request.GET['머리띠사자']
    teamh = request.GET['모자사자']
    teamf = request.GET['꽃사자']
    team.append(teamg)
    team.append(teamb)
    team.append(teamh)
    team.append(teamf)
    m = 0
    colorn = []
    for t in team:
        if t == 'white':
            colorn.append(11)
        elif t == 'yellow':
            colorn.append(10)
        elif t == 'red':
            colorn.append(9)
        elif t == 'green':
            colorn.append(8)
        elif t == 'blue' :
            colorn.append(6)
        else :
            colorn.append(0)
   

    for c in colorn:
        if c >= m:
            m = c
        
    
    if m == 11:
        result = 'white'
    elif m == 10:
        result = 'yellow'
    elif m == 9:
        result = 'red'
    elif m == 8:
        result = 'green'
    elif m == 6 :
        result = 'blue'
    else :
        result = 'black'

    if colorn[0] == m:
        l = Team.objects.get(title = '안경사자')
        l.score += int(request.GET['score'])
        l.save()
    
    if colorn[1] == m:
        l = Team.objects.get(title = '머리띠사자')
        l.score += int(request.GET['score'])
        l.save()
    if colorn[2] == m:
        l = Team.objects.get(title = '모자사자')
        l.score += int(request.GET['score'])
        l.save()
    if colorn[3] == m:
        l = Team.objects.get(title = '꽃사자')
        l.score += int(request.GET['score'])
        l.save()

    
    context = { 'result' : result }

    return render(request,'mta/result.html',context)

# Create your views here.
