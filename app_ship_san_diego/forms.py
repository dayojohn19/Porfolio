
from django import forms
from .models import MySanDiegoDays, MySandiegoGallery


class DaysForm(forms.ModelForm):
    class Meta:
        model = MySanDiegoDays
        fields = ('title', 'feeling', 'country',
                   'image')

class GalleryForm(forms.ModelForm):
    model = MySandiegoGallery
    fields = ('title', 'description','value','location')
