from django.shortcuts import render

# Create your views here.
def app_mail(request):
    return render(request, 'application/mail/inbox.html')

def application(request):
    return render(request, 'application/application.html')