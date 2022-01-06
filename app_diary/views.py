from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'template_name')

def index(request):
    return render(request, 'application/diary/index.html')
