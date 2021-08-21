from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'games/games.html')
def addition(request):
    return render(request, 'games/addition.html')
def color_game(request):
    return render(request, 'games/color_pigeon/color_pigeon.html')