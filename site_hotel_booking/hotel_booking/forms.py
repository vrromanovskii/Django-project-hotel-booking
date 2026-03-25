from django import forms
from .models import *

class BookingForm(forms.ModelForm):
    class Meta:
        model = Bookings
        fields = ['room', 'guest_name', 'check_in', 'check_out']
        widgets = {
            'check_in': forms.DateInput(attrs={'type': 'date'}),
            'check_out': forms.DateInput(attrs={'type': 'date'}),
        }


class HotelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = ['name', 'price']
        widgets = {
            'price': forms.NumberInput(attrs={'step': '1'}),
        }