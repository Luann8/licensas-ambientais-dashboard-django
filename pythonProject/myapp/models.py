from django.db import models

class LicencaAmbiental(models.Model):
    numero_licenca = models.CharField(max_length=100)
    prazo = models.DateField()
    descricao = models.TextField()

    def __str__(self):
        return self.numero_licenca
