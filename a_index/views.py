from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'a_index/index.html', {})

def social(request):
    return render(request, 'a_index/social.html')

def colreg(request):
    return render(request, 'a_index/colregs.html')

def blog(request):
    return render(request, 'a_index/blog.html')