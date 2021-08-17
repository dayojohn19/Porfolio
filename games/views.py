from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'games/games.html')
def addition(request):
    return render(request, 'games/addition.html')