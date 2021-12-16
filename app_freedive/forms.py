from django import forms


class Send_Message(forms.Form):

    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'django-text', 'id': 'django-message', 'name': 'django-send'
    }))
