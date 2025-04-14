from django.db import models
from django.forms import CharField

class Editora(models.model):
    nome = CharField(max_length=100)

    def __str__(self):
        return f"{self.descricao} ({self.id})"