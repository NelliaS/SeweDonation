from dataclasses import fields
from django import forms
from .models import OrganisationProfile


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model   = OrganisationProfile
        fields  = ('organisation_name', 'contact_person',  'phone', 'email', 'password', 'address')

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

class LogInForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model   = OrganisationProfile
        fields  = ('email', 'password')

    def __init__(self, *args, **kwargs):
        super(LogInForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-floating mb-2 text-secondary'



#class LogIn(forms.Form):
 #   username    = forms.EmailField
  #  password    = forms.PasswordInput