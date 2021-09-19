from django.shortcuts import render

# Create your views here.
def app_mail(request):
    if request.user.is_authenticated:
        return render(request, 'mail/inbox.html')
    return render(request, 'mail/login.html')

def application(request):
    return render(request, 'application/application.html') 

def news(request):
    return render(request, 'news/index.html')
def course_booking(request):
    return render(request, 'course_booking/index.html')
def blog(request):
    return render(request, 'blog/blog.html')