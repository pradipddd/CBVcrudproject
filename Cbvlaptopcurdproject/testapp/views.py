from django.shortcuts import render
from .forms import LaptopModelForm
from .models import Laptop
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView

# Create your views here.

class LaptopListView(ListView):
    model=Laptop

class LaptopCreateView(CreateView):
    model=Laptop
    fields='__all__'
    success_url='/laptop/list'

class LaptopUpdateView(UpdateView):
    model=Laptop
    fields='__all__'
    success_url='/laptop/list'

class LaptopDeleteView(DeleteView):
    model=Laptop
    success_url='/laptop/list'




