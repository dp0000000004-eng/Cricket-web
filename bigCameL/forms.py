from .models import TotalBooked, TotalSit
from django import forms
from django.contrib.auth.models import User


class BookingForm(forms.ModelForm):
    class Meta:
        vip_sit = int(TotalSit.objects.first().vip)
        normal_sit = int(TotalSit.objects.first().normal)

        if vip_sit > 0 and normal_sit > 0:
            model = TotalBooked
            fields = ['vip','normal']
            labels = {
                'vip': 'Book Vip Sit: ',
                'normal': 'Book normal Sit: ',
            }
            widgets = {
                "vip":forms.NumberInput(attrs={'min':0}),
                "normal":forms.NumberInput(attrs={'min':0})
            }
        elif vip_sit > 0 and normal_sit == 0:
            model = TotalBooked
            fields = ['vip']
            widgets = {
                "vip":forms.NumberInput(attrs={'min':0})
            }
        elif vip_sit == 0 and normal_sit > 0:
            model = TotalBooked
            fields = ['normal']
            widgets = {
                "normal":forms.NumberInput(attrs={'min':0})
            }


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email", "password"]
        widgets = {
            "password":forms.PasswordInput(attrs={'minlength':8})
        }
