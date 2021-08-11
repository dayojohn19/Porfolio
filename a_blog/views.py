from django.shortcuts import render

##importing forms
from django import forms
#get util.py
from . import util
# Create your views here.


def index(request):
    return render(request, 'a_blog/index.html', {
        'form':Search(), "post":Post(),
        "entries": util.list_entries()
    })

from markdown2 import Markdown
markdowner = Markdown()
class Post(forms.Form):
    title = forms.CharField(label= "Title")
    pan = forms.CharField(label= "pan")
    img = forms.ImageField()
    textarea = forms.CharField(widget=forms.Textarea(), label='')
class Search(forms.Form):
    item = forms.CharField(widget=forms.TextInput(attrs={'class' : 'myfieldclass', 'placeholder': 'Search'}))
def save_blog(request):
    if request.method == 'POST':
        form = Post(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            t1 = form.cleaned_data["textarea"]
            pan = form.cleaned_data["pan"]
            img = form.cleaned_data["img"]
            textarea = t1 +  ' by -' + pan + img
            entries = util.list_entries()
            if title in entries:
                return render(request, 'a_blog/index.html',{
                    'message':'Sorry already has the same Title'
                })
            else:
                #save the new
                util.save_entry(title, textarea, pan)
                page = util.get_entry(title)
                page_converted = markdowner.convert(page)

                context = {
                    'form':Search(),
                    'page':page_converted,
                    'title':title
                }
                return render(request, 'a_blog/index.html', {'message':'success'})
        else:
            return render(request, 'a_blog/index.html', {
            'message':'error sorry'
        })
    else:
        return render(request, 'a_blog/index.html', {
            'message':'not Post'
        })