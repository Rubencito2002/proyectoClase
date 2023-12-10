from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Aula, ReservaAula
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView

class lista_aulas(ListView):
    model = Aula
    template_name = 'appreserva/lista_aulas.html'

class reserva_aula(CreateView):
    model = ReservaAula
    fields = ['aula', 'fecha_inicio', 'fecha_fin', 'nombre_reservante', 'email_reservante', 'hora_inicio', 'hora_fin']
    template_name = 'appreserva/reserva_aula.html'
    success_url = reverse_lazy('lista_aulas')

class crear_aula(CreateView):
    model = Aula
    fields = ['nombre', 'capacidad']
    template_name = 'appreserva/crear_aula.html'
    success_url = reverse_lazy('lista_aulas')

class detail_aula(DetailView):
    model = Aula
    template_name = 'appreserva/details_aula.html'

class edit_aula(UpdateView):
    model = Aula
    template_name = 'appreserva/edit_aula.html'
    success_url = reverse_lazy('lista_aulas')

class delete_aula(DeleteView):
    model = Aula
    template_name = 'appreserva/delete_aula.html'
    success_url = reverse_lazy('lista_aulas')