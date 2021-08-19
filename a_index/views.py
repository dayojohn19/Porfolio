from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'a_index/index.html', {})

def social(request):
    return render(request, 'social/social.html')

def colreg(request):
    return render(request, 'colregs/colregs.html')

def blog(request):
    return render(request, 'blog/blog.html')

def map(request):
    return render(request, 'map/map.html')
def games(request):
    return render(request, 'games/games.html')
def application(request):
    return render(request, 'application/application.html')
