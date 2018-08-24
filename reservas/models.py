from django.db import models
from associados.models import Associado
from enum import Enum

# Create your models here.
class Reserva(models.Model):
    Apartamento = 'Apartamento'
    Casa = 'Casa'
    Chalé = 'Chalé'
    EscolhaAmbiente = (
        (Apartamento, 'Apartamento'),
        (Casa, 'Casa'),
        (Chalé, 'Chalé'),
    )
    Sim = 'Sim'
    Não = 'Não'
    NecessidadeEspecial = (
    	(Sim, 'Sim'),
    	(Não, 'Não'),
    )
    Agendado = 'Agendado'
    Cancelado = 'Cancelado'
    Confirmado = 'Confirmado'
    Espera = 'Espera'
    EscolhaSituacao = (
    	(Agendado, 'Agendado'),
    	(Cancelado, 'Cancelado'),
    	(Confirmado, 'Confirmado'),
    	(Espera, 'Espera'),
    )
    associado = models.ForeignKey(Associado, on_delete=models.CASCADE, verbose_name = 'Associado')
    dataAgendamento = models.DateField('Data de Agendamento')
    dateEntrada = models.DateField('Data de Entrada')
    dateSaida = models.DateField('Data de Saída')
    ambiente = models.CharField(
        'Ambiente',
        max_length=11,
        choices=EscolhaAmbiente
    )
    necessidade = models.CharField(
        'Necessidade Especial',
        max_length=11,
        choices=NecessidadeEspecial
    )
    situacao = models.CharField(
        'Situação',
        max_length=11,
        choices=EscolhaSituacao
    )
    def __str__(self):
        return self.ambiente
