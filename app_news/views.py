from django.shortcuts import render
from .models import Article
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

######
from django import forms

class ArticleForm(forms.Form):
    sections=('1', 'Political'), ('2', 'Sports'),('3','Health'),('4','Military'),('5','Business'),('6','Lifestyle'),('7','Biography'),('8','Maritime'),('9','Personal Growth'),('10','Farm'),('101','Others')
    title = forms.CharField(label="Title")
    link = forms.CharField(label="link")
    content = forms.CharField(label="Content",widget=forms.TextInput(attrs={'class': 'special'}))
    section = forms.ChoiceField(widget=forms.RadioSelect,choices=sections)


######
# Create your views here.


def index(request):
    contents = {
        'articles':Article.objects.all().order_by('id').reverse(),
        'form':ArticleForm()
    }
    return render(request, 'news/index.html', contents)

def section(request, x):
    contents = Article.objects.filter(section=x).order_by('id').reverse()
    return render(request, 'news/index.html', {
        'articles':contents
    })


def publish(request):
    if request.user.is_anonymous:
        return HttpResponseRedirect(reverse("sale:login"))
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            art = Article (
                author = request.user,
                title = form.cleaned_data["title"],
                link = form.cleaned_data["link"],
                content = form.cleaned_data["content"],
                section = form.cleaned_data["section"]
            )
            art.save()
            contents = {
                'articles':Article.objects.all().order_by('id').reverse(),
            }
            return HttpResponseRedirect(reverse("news:index"))
        else:
            return render(request, "news/publish.html", {
                "form": form
            })
    else:
        return render(request, 'news/publish.html', {'form':ArticleForm()})
    
