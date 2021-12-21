from django.shortcuts import render, redirect

# Create your views here.


def app_mail(request):
    if request.user.is_authenticated:
        return render(request, 'mail/inbox.html')
    return render(request, "user/login.html")

    # return redirect('user:index')

    # return render(request, 'mail/login.html')


def application(request):
    return render(request, 'application/application.html')


def news(request):
    return render(request, 'news/index.html')


def course_booking(request):
    return redirect('news:index')

    # return render(request, 'course_booking/index.html')
