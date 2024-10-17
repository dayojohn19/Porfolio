from datetime import date
from django import forms
from .models import PlaceSchedule, placeEvent


class PlaceEventForm(forms.ModelForm):
    class Meta:
        model = placeEvent
        fields = ('dateN', 'monthN', 'yearN', 'meetPlace', 'meetTime',
                  'endDate', 'eventTitle', 'eventCost', 'eventDetails',)


class PlaceScheduleForm(forms.ModelForm):

    class Meta:
        model = PlaceSchedule
        fields = ('monthN', 'dateN', 'timeDeparture', 'departFrom',
                  'contactNumber', 'otherDetails',)
        widgets = {
            'departFrom': forms.TextInput({'placeholder': 'Province, Municipality, Others'}),
            'timeDeparture': forms.TextInput({'placeholder': 'example: 1:00 to 2:30 pm'}),
            'monthN': forms.TextInput({'placeholder': 'Month Number'}),
            'contactNumber': forms.TextInput({'placeholder': 'Your Contact Details'}),
            'otherDetails': forms.Textarea({'placeholder': 'Details of Schedule & FaceBook Account (optional) '})

        }   
