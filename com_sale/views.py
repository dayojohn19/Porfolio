from django.shortcuts import render
from django import forms
from com_sale.models import Item, Order
from django.shortcuts import redirect
from django.http import HttpResponse
from app_mail.models import User
class Sale(forms.Form):
    cat=('1', 'Service'), ('2', 'Goods')
    title = forms.CharField(label="Title")
    link = forms.CharField(label="link")
    link2 = forms.CharField(label="link")
    link3 = forms.CharField(label="link")
    link4 = forms.CharField(label="link")
    link5 = forms.CharField(label="link")
    link6 = forms.CharField(label="link")
    link7 = forms.CharField(label="link")
    link8 = forms.CharField(label="link")
    link9 = forms.CharField(label="link")
    link10 = forms.CharField(label="link")
    price = forms.IntegerField()
    description = forms.CharField(label="Description",widget=forms.TextInput(attrs={'class': 'special'}))
    category = forms.ChoiceField(widget=forms.RadioSelect,choices=cat)

    

def add_check(user, hashed, i_price):
    ####### update value
    if hashed != user.first_name:
        return ('hacker')
    else:
        new_hash = hash(str(hashed))
        user.first_name = new_hash
        user.last_name = int(user.last_name) + i_price
        user.save()
    
    ######## end update value
def sub_check(user, hashed, i_price):
    ####### update value
    if hashed != user.first_name:
        return ('hacker')
    if int(user.last_name) <= 0 :
        return ('poor')
    else:
        new_hash = hash(str(hashed))
        user.first_name = new_hash
        value = int(user.last_name) - i_price
        if value <= 0:
            return value
        user.last_name = value
        user.save()
        return value
    ######## end update value
def reload(user, hashed, load, target):
    #### add object that error when less than 0
    if hashed != user.first_name:
        return ('hacker')
    new_hash = hash(str(hashed))
    user.first_name = new_hash
    user.last_name = int(user.last_name) - int(load)
    user.save()
    target.first_name = new_hash
    target.last_name = int(target.last_name) + int(load)
    target.save()
def load(request):
    if request.method == 'POST':
        user = request.user
        hashed = user.first_name
        load = request.POST.get("load")
        target = User.objects.get(username=request.POST.get("target"))
        value = reload(user, hashed, load, target)
        if value == 'hacker':
            return HttpResponse('error')
        return HttpResponse('reloaded the target')
# Create your views here.
def index(request):
    return render(request, 'commerce/sale/index.html', {
        'item':Item.objects.all().order_by('id').reverse(),
        'users':User.objects.all()
    })

def item(request, id):
    # return render(request, 'commerce/sale/item.html')
    # return redirect('sale:index')

    items = Item.objects.get(id=id)
    return render(request, 'commerce/sale/item.html',{
        'item':Item.objects.get(id=id),
        'ordered':Order.objects.filter(item=items)
    })

def create(request):
    if request.method == 'POST':
        form = Sale(request.POST)
        if form.is_valid():
            value = int(form.cleaned_data["price"])
            o = Item(
            owner = request.user,
            link = form.cleaned_data["link"],
            link2 = form.cleaned_data["link2"],
            link3 = form.cleaned_data["link3"],
            link4 = form.cleaned_data["link4"],
            link5 = form.cleaned_data["link5"],
            link6 = form.cleaned_data["link6"],
            link7 = form.cleaned_data["link7"],
            link8 = form.cleaned_data["link8"],
            link9 = form.cleaned_data["link9"],
            link10 = form.cleaned_data["link10"],
            title= form.cleaned_data["title"],
            description = form.cleaned_data["description"],
            price = value,
            category = form.cleaned_data["category"]
            )

            ## reduce the users' value
            v = request.user
            newValue = int(request.user.last_name) - value 
            if newValue <= 0:
                return render(request, 'commerce/sale/create.html',{
                # return redirect('sale:item', o.id)
                'message':'Please Reload Insufficient Balance',
                'form':form
            })
            v.first_name = hash(str(newValue))
            v.last_name = newValue
            v.save()
            ## save the listing
            o.save()
            return redirect('sale:item', o.id)
        else:
            return render(request, 'commerce/sale/create.html',
            {
                'form':form,
                'message':'form not valid'
            })        
    return render(request, 'commerce/sale/create.html',{
        'form':Sale()
    })

def order(request, item_id, hashed, i_price):
    if request.user.is_anonymous:
        return redirect('mail:login')
    user = request.user
    if request.method == 'GET':
        # item_id = request.GET['item_id']
        order = Item.objects.get(id=item_id)
        user = request.user

        if order.notavailable == False:
            if user in order.orders.all():
                if add_check(user, hashed, i_price) == 'hacker':
                    return HttpResponse('hacked')
                ######## end update value
                o = Order.objects.get(item=order, user=user)
                if o.delivered == True:
                    return HttpResponse('Fail to Unorder, Item already delivered')
                o.delete()
                order.orders.remove(user)
                ####### update value
                return redirect('sale:item', item_id)
            else:
                ####### update value
                v = sub_check(user, hashed, i_price)
                if v == 'hacker':
                    return HttpResponse('hacked')
                elif v <= 0:
                    return HttpResponse('poor')
                ######## end update value
                o = Order.objects.create(user=user, item=order)
                order.orders.add(user)
                order.save()

                return redirect('sale:item', item_id)
        else:
            return redirect('sale:item', item_id)
            # return HttpResponse('fail Already Delivered')
    ### get user items
    elif request.method == 'POST':
        items = Item.objects.get(id=item_id)
        content = {
        'item' : Item.objects.get(id=item_id),
        'ordered' : Order.objects.all()
        }
    return redirect('sale:item', item_id)


