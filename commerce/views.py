from django.shortcuts import render

# Create your views here.
def commerce(request):
    return render(request, 'commerce/commerce.html')
def auction(request):
    return render(request, 'auction/index.html')




from app_mail.models import User
def last_name(request):
    if request.method == 'POST':
        user = User.objects.get(pk=request.user.id)
        lastname = request.POST.get("last_name")
        user.last_name = int(lastname) + int(user.last_name)
        user.save()
    return render(request, 'commerce/commerce.html', {
        'new':User.objects.get(pk=request.user.id),
        'last':user.last_name
    })
