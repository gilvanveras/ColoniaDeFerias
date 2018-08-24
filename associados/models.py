from django.db import models
from .helper import validate_CPF
from .helper import validate_CONTACT

class Associado(models.Model):
    matricula = models.BigIntegerField('Matrícula')
    nome = models.CharField('Nome', max_length=254)
    categoria = models.CharField('Nome', max_length=254)
    #cpf = models.CharField('CPF', unique=True, max_length=14, validators=[validate_CPF])
    cpf = models.CharField('Nome', max_length=254)
    #contato = models.CharField('Contato', unique=True, max_length=14, validators=[validate_CONTACT])
    contato = models.CharField('Nome', max_length=254)
    email = models.EmailField('Email', max_length=254)
    lotacao = models.CharField('Lotação', max_length=254)
    comarca = models.CharField('Comarca', max_length=254)

    def __str__(self):
        return self.nome