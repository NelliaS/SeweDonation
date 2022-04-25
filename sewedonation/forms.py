from dataclasses import fields
from socket import fromshare
from ssl import _PasswordType
from django import forms
from .models import OrganisationProfile


class RegistrationForm(forms.ModelForm):
    
    class Meta:
        model   = OrganisationProfile
        fields  = ('organisation_name', 'username', 'contact_person', 'address', 'phone', 'notes')


#class LogIn(forms.Form):
 #   username    = forms.EmailField
  #  password    = forms.PasswordInput