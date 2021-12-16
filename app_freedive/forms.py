from django import forms
from .models import Event_Picture


class Send_Message(forms.Form):

    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'django-text', 'id': 'django-message', 'name': 'django-send'
    }))


class Event_Image(forms.ModelForm):
    class Meta:
        model = Event_Picture
        fields = ('image',)
