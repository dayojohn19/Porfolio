from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'application/freedive/index.html')


def home(request):
    return render(request, 'application/freedive/home.html')


def events(request):
    return render(request, 'application/freedive/events.html')


def socials(request):
    return render(request, 'application/freedive/socials.html')


def community(request):
    return render(request, 'application/freedive/community.html')
