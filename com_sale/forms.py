from django import forms
from .models import Image, Userimage

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('name', 'image')

class UserImageForm(forms.ModelForm):
    class Meta:
        model = Userimage
        fields = ('name', 'image')