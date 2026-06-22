from .models import TotalBooked
from django import forms


class BookingForm(forms.ModelForm):
    class Meta:
        model = TotalBooked
        fields = ['vip','normal']