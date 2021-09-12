from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.
def commerce(request):
    return render(request, 'commerce/commerce.html')
def auction(request):
    return render(request, 'commerce/auction/index.html')
def sale(request):
    return redirect('sale:index')




