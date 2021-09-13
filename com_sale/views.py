from django.shortcuts import render
from django import forms
from com_sale.models import Item, Order
from django.shortcuts import redirect
from django.http import HttpResponse
from app_mail.models import User
import datetime
class Sale(forms.Form):
    cat=('1', 'Service'), ('2', 'Goods')
    title = forms.CharField(required=True ,label="Title")
    link = forms.CharField(required=True ,label="link", widget=forms.TextInput(attrs={'placeholder': 'Picture Link'}))
    link2 = forms.CharField(required=False, label="link",widget=forms.TextInput(attrs={'placeholder': 'Picture Link (Optional)'}))
    link3 = forms.CharField(required=False, label="link2",widget=forms.TextInput(attrs={'placeholder': 'Picture Link (Optional)'}))
    link4 = forms.CharField(required=False, label="link3",widget=forms.TextInput(attrs={'placeholder': 'Picture Link (Optional)'}))
    link5 = forms.CharField(required=False, label="link4",widget=forms.TextInput(attrs={'placeholder': 'Picture Link (Optional)'}))
    link6 = forms.CharField(required=False, label="link5",widget=forms.TextInput(attrs={'placeholder': 'Picture Link (Optional)'}))
    link7 = forms.CharField(required=False, label="link6",widget=forms.TextInput(attrs={'placeholder': 'Picture Link (Optional)'}))
    link8 = forms.CharField(required=False, label="link7",widget=forms.TextInput(attrs={'placeholder': 'Picture Link (Optional)'}))
    link9 = forms.CharField(required=False, label="link8",widget=forms.TextInput(attrs={'placeholder': 'Picture Link (Optional)'}))
    link10 = forms.CharField(required=False, label="link9",widget=forms.TextInput(attrs={'placeholder': 'Picture Link (Optional)'}))
    price = forms.IntegerField(required=True)
    description = forms.CharField(required=True ,label="Description",widget=forms.TextInput(attrs={'class': 'special'}))
    category = forms.ChoiceField(required=True ,widget=forms.RadioSelect,choices=cat)




def mylist(request):
    filtered = Item.objects.filter(owner=request.user).order_by('id').reverse()
    contents = {
        'items':filtered
    }
    return render(request, 'commerce/sale/mylist.html', contents)
def myorder(request):
    filtered = Order.objects.filter(user=request.user).order_by('id').reverse()
    contents = {
        'items':filtered
    }
    return render(request, 'commerce/sale/myorder.html', contents)
def mybuyer(request):
    ##  Post Deliver
    if request.method == 'POST':
        item_id = request.POST.get("item_id")
        x = Order.objects.get(id=item_id)
        user = x.user
        order = Item.objects.get(id=x.i_id)
        order_price = int(order.price) * int(x.qty)
        add_check(request.user, request.user.first_name, order_price)
        if user in order.orders.all():
            o = Order.objects.get(item = order, user=user, delivered=False)
            o.delete()
            order.orders.remove(user)
            order.bought= int(order.bought) + int(x.qty)
            order.save()
            x.delivered = True
            x.del_time = datetime.datetime.now()
            x.save()
            return redirect('sale:mybuyer')
    ## end POST deliver
    filtered = Order.objects.filter(owner=request.user).order_by('id').reverse()
    contents = {
        'items':filtered,
        'date':datetime.datetime.now()
    }
    return render(request, 'commerce/sale/mybuyer.html',contents)

def add_check(user, hashed, i_price):
    ####### update value
    if hashed != user.first_name:
        return ('hacker')
    else:
        new_hash = hash(str(hashed))
        user.first_name = new_hash
        user.last_name = int(user.last_name) + int(i_price)
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
        owner = order.owner
        time = datetime.datetime.now()
        select = request.GET.get("select")
        qty = request.GET.get("qty")
        i_price = i_price * int(qty)
        if order.notavailable == False:
            if user in order.orders.all():
                if add_check(user, hashed, i_price) == 'hacker':
                    return HttpResponse('hacked')
                ######## end update value
                o = Order.objects.get(i_id=order.id, item=order, user=user, delivered=False)
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
                elif v == 'poor':
                    return HttpResponse('poor')
                elif v <= 0:
                    return HttpResponse('poor')
                ######## end update value
                o = Order.objects.create(i_id=order.id, user=user, item=order, select=select, qty=qty, owner=order.owner, time=time)
                order.orders.add(user)
                order.save()

                return redirect('sale:myorder')
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


