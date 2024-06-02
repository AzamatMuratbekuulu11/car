from django.urls import reverse_lazy

from .models import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .forms import CarForms

class ShopListView(ListView):
    queryset = Car.objects.all()
    template_name = 'shop_list.html'
    context_object_name = 'shop'

class ShopDetailView(DetailView):
    queryset = Car.objects.all()
    template_name = 'shop_detail.html'
    context_object_name = 'shop'

class ShopCreateView(CreateView):
    template_name = 'shop_create.html'
    form_class = CarForms
    success_url = reverse_lazy('shop_list')

class ShopUpdateView(UpdateView):
    queryset = Car.objects.all()
    template_name = 'shop_update.html'
    form_class = CarForms
    success_url = reverse_lazy('shop_list')

class ShopDeleteView(DetailView):
    queryset = Car.objects.all()
    template_name = 'shop_delete.html'
    success_url = reverse_lazy('shop_list')