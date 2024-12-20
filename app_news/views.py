import requests
from django.shortcuts import render
from .models import Article
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

######
from django import forms


class ArticleForm(forms.Form):
    sections = ('1', 'Political'), ('2', 'Sports'), ('3', 'Health'), ('4', 'Military'), ('5', 'Business'), ('6',
                                                                                                            'Lifestyle'), ('7', 'Biography'), ('8', 'Maritime'), ('9', 'Personal Growth'), ('10', 'Farm'), ('101', 'Others')
    title = forms.CharField(label="Title", widget=forms.TextInput(
        attrs={'class': 'form_title', 'placeholder': 'Title'}))
    content = forms.CharField(label="link", widget=forms.Textarea(
        attrs={'class': 'form_content'}))
    link = forms.CharField(
        label="Content", widget=forms.TextInput(attrs={'class': 'form_textarea', 'placeholder': 'Input your link here'}))
    section = forms.ChoiceField(widget=forms.RadioSelect(
        attrs={'class': 'form_section'}), choices=sections)


######
# Create your views here.

# !NOTE !NOTE IMPORTANT
# To get LATEST NEWS
# removed the lates news
# LATEST_NEWS = requests.get(
#     'https://newsapi.org/v2/top-headlines?country=ph&apiKey=b3f57b413e2942cc94bd6609ed38a52f').json()

# ****************** https://newsapi.org/docs/get-started


def index(request):
    contents = {
        'articles': Article.objects.all().order_by('id').reverse(),
        'form': ArticleForm()
    }
    return render(request, 'news/index.html', contents)


def section(request, x):
    contents = Article.objects.filter(section=x).order_by('id').reverse()
    return render(request, 'news/index.html', {
        'articles': contents
    })


def publish(request):
    if request.user.is_anonymous:
        return HttpResponseRedirect(reverse("user:login"))
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            art = Article(
                author=request.user,
                title=form.cleaned_data["title"],
                link=form.cleaned_data["link"],
                content=form.cleaned_data["content"],
                section=form.cleaned_data["section"]
            )
            art.save()
            contents = {
                'articles': Article.objects.all().order_by('id').reverse(),
            }
            return HttpResponseRedirect(reverse("news:index"))
        else:
            return render(request, "news/publish.html", {
                "form": form
            })
    else:
        return render(request, 'news/publish.html', {'form': ArticleForm()})
