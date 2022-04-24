from django.shortcuts import render
from .models import ItemVariation, Item

# Create your views here.

def overview(request):
    items_list = ItemVariation.objects.all().order_by('saldo')
    three_lowest = items_list[0:3]
    return render(request, 'sewedonation/overview.html', {'three_lowest': three_lowest})


def register(request):
    return render(request, 'sewedonation/registration.html')

def login(request):
    return render(request, 'sewedonation/login.html')

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
