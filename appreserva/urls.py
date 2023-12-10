from django.urls import path
from .views import lista_aulas, reserva_aula, crear_aula, detail_aula, edit_aula, delete_aula

urlpatterns = [
    path('', lista_aulas.as_view() , name='lista_aulas'),
    path('reservar/', reserva_aula.as_view() , name='reserva_aula'),
    path('crearAula/', crear_aula.as_view(), name='crear_aula'),
    path('details/<int:pk>/', detail_aula.as_view(), name='detail_aula'),
    path('edit/<int:pk>/', edit_aula.as_view(), name='edit_aula'),
    path('delete/<int:pk>/', delete_aula.as_view(), name='delete_aula'),
]