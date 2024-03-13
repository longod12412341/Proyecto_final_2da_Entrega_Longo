from django.shortcuts import render
from app1.models import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
#Celulares Nuevos
     
class celularNuevoListView(ListView):
     model = celularnuevo
     template_name = "app1/celularNuevo_list.html"


class celularNuevoDetailView(LoginRequiredMixin,DetailView):
    model = celularnuevo
    template_name = "app1/celularNuevo_detalle.html"


class celularNuevoCreateView(LoginRequiredMixin,CreateView):
     model = celularnuevo 
     success_url = reverse_lazy("nuevoLista")
     fields = "__all__"

class celularNuevoUpdate(LoginRequiredMixin,UpdateView):
     model = celularnuevo
     success_url = reverse_lazy("nuevoLista")
     fields= ["email","descripcion","telefono", "precio", "estado", "imagen"]

class celularNuevoDelete(LoginRequiredMixin,DeleteView):
     model = celularnuevo
     success_url = reverse_lazy("nuevoLista")
     template_name = "app1/celularNuevo_confirm_delete.html"