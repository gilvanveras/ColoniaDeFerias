from django.urls import path
from .views import list_reservas, create_reserva, update_reserva, delete_reserva

urlpatterns = [
    path('', list_reservas, name='list_reservas'),
    path('nova/', create_reserva, name='create_reserva'),
    path('atualizar/<int:id>/', update_reserva, name='update_reserva'),
    path('deletar/<int:id>/', delete_reserva, name='delete_reserva'),
]


# CRUD - CREATE, READ, UPDATE, DELETE