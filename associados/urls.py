from django.urls import path
from .views import list_associados, create_associado, update_associado, delete_associado

urlpatterns = [
    path('', list_associados, name='list_associados'),
    path('novo/', create_associado, name='create_associado'),
    path('atualizar/<int:id>/', update_associado, name='update_associado'),
    path('deletar/<int:id>/', delete_associado, name='delete_associado'),
]


# CRUD - CREATE, READ, UPDATE, DELETE