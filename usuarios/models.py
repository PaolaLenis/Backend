from django.db import models
from rest_framework.reverse import reverse as api_reverse

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    uid = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    edad = models.CharField()
    genero = models.CharField(max_length=15)
    peso = models.CharField(max_length=15)
    altura = models.CharField(max_length=15)
    enfermedad = models.CharField(max_length=100)

    def get_api_url(self, request=None):
        return api_reverse("", kwargs={'uid': self.uid}, request=request)

    def __unicode__(self):
        return self.nombre

    def __str__(self):
        return self.nombre
