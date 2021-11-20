from markdown2 import Markdown
from django.shortcuts import render
from .models import Blog_item

# importing forms
from django import forms
# get util.py
from . import util
# Create your views here.


def blog(request):
    context = {
        'blogs': 'hey',
        'blogs': Blog_item.objects.all().order_by('id').reverse()
    }
    return render(request, 'blog/blog.html', context)


def index(request):
    return render(request, 'blog/index.html', {
        'form': Search(),
        "post": Post(),
        # 'blogs': Blog_item.objects.all()


        # "entries": util.list_entries()
    })


markdowner = Markdown()


class Post(forms.Form):

    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form_title',
                'placeholder': 'title',

            }
        ),
        label="")
    pan = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form_pan',
                'placeholder': 'Sub Title',
            }
        ), label="")
    # img = forms.ImageField()
    textarea = forms.CharField(
        label='',
        widget=forms.Textarea(
            attrs={'placeholder': 'Text Area', 'class': 'form_textarea'}
        )
    )


class Search(forms.Form):
    item = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'myfieldclass', 'placeholder': 'Search'}))


def get_blog(request):
    blog = util.list_entries()
    return blog


def save_blog(request):
    if request.method == 'POST':
        form = Post(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            t1 = form.cleaned_data["textarea"]
            pan = form.cleaned_data["pan"]

            # img = form.cleaned_data["img"]
            # textarea = t1 +  ' by -' + pan + img
            textarea = t1 + ' by -' + pan
            entries = util.list_entries()
            if title in entries:
                return render(request, 'blog/index.html', {
                    'message': 'Sorry already has the same Title',
                    "post": form
                })
            else:
                # save the new
                # model
                # blog = Blog_item(
                #     title=title,
                #     sub_title=pan,
                #     paragraph=t1,
                #     picture_link=request.POST["link"]
                # )
                # blog.save
                blog = Blog_item()
                blog.title = title
                blog.sub_title = pan
                blog.paragraph = t1
                blog.picture_link = request.POST["link"]
                blog.save()

                util.save_entry(title, textarea, pan)
                page = util.get_entry(title)
                page_converted = markdowner.convert(page)

                context = {
                    # 'form': Search(),
                    'page': page_converted,
                    'title': title
                }
                return render(request, 'blog/index.html', context)
        else:
            return render(request, 'blog/index.html', {

                'message': 'error sorry'
            })
    else:
        return render(request, 'blog/index.html', {
            'message': 'not Post'
        })
