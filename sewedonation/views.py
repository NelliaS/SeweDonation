from django.shortcuts import render, redirect
from .models import ItemVariation, OrganisationProfile
from .forms import RegistrationForm
from django.contrib.auth import authenticate, login

# Create your views here.

def overview(request):
    if request.method == 'POST':
      email = request.POST['email']           # v závorce název fieldu
      password = request.POST['password']
      user = authenticate(email=email, password=password)      # vrátí user object
      
      if user is not None:
        login(request, user)
        return redirect('overview')     # ZMĚNIT PAK NA STOCK
      else:
        return redirect('overview')
        
    
    items_list = ItemVariation.objects.all().order_by('saldo')
    three_lowest = items_list[0:3]
    return render(request, 'sewedonation/overview.html', {'three_lowest': three_lowest})

def registration(request):
    if request.method == 'POST':
      form = RegistrationForm(request.POST)   # bude obsahovat všechny hodnoty polí
      if form.is_valid():                     # má všechna povinná pole vyplněná
          organisation_name   = form.cleaned_data['organisation_name']
          contact_person      = form.cleaned_data['contact_person']
          phone               = form.cleaned_data['phone']
          email               = form.cleaned_data['email']
          username            = (email.split("@")[1]).split(".")[0]
          password            = form.cleaned_data['password']
          address             = form.cleaned_data['address']
          
          user = OrganisationProfile.objects.create_user(organisation_name=organisation_name, email=email, username=username, password=password)
          user.phone = phone
          user.contact_person = contact_person
          user.address = address
          user.save()
          return render(request, 'sewedonation/registration_succeed.html')
    else:
      form = RegistrationForm()
      return render(request, 'sewedonation/registration.html', {'form': form})

def registration_succeed(request):
    return render(request, 'sewedonation/registration_succeed.html')

def logout(request):
    return render(request, 'sewedonation/logout.html')
        





        #def get_available_quantity(self):
     #   _ = self.on_stock - self.reserved_quantity
      #  if _ <= 0:
    #        available_quantity = 0
     #   else:
      #      available_quantity = _
       # return available_quantity


    #available_quantity = self.get_available_quantity()
