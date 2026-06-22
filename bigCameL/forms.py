from .models import TotalBooked
from django import forms
from django.contrib.auth.models import User


class BookingForm(forms.ModelForm):
    class Meta:
        model = TotalBooked
        fields = ['vip','normal']
        widgets = {
            "vip":forms.NumberInput(attrs={'min':0}),
            "normal":forms.NumberInput(attrs={'min':0})
        }


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email", "password"]
        widgets = {
            "password":forms.PasswordInput(attrs={'minlength':8})
        }

        def save(self, commit=True):
            user = super().save(commit=False)
            user.set_password(self.cleaned_data["password"])
            if commit:
                user.save()
                
            return user