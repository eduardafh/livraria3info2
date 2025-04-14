from django.db import models
from django.forms import CharField
from .categoria import Categoria
from .editora import Editora

class Livro(models.Model):
    titulo = CharField(max_length=255)
    isbn = models.CharField(max_length=32, null=True, blank=True)
    quantidade = models.IntegerField(default=0, null=True, blank=True)
    preco = models.CharField(max_length=100)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.PROJECT, related_name="livros", null=True, blank=True
    )
    editora = models.ForeignKey(Editora, on_delete=models.PROTECT, related_name="livros", null=True, blank=True)


    def __str__(self):
        return f"{self.descricao} ({self.id})"