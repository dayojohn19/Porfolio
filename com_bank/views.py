from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'commerce/bank/index.html')

def account (request,csrf_token):
    return render(request, 'commerce/bank/account.html')

def schedule (request,csrf_token):
    return render(request, 'commerce/bank/schedule.html')

def manager (request,csrf_token):
    return render(request, 'commerce/bank/manager.html')

def client (request,csrf_token):
    return render(request, 'commerce/bank/client.html')