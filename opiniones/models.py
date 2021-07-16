from django.db import models
from usuarios.models import Usuario
from rest_framework.reverse import reverse as api_reverse

# Create your models here.
class Opinion(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    

    def get_api_url(self, request=None):
        return api_reverse("", kwargs={'id': self.id}, request=request)

    def __unicode__(self):
        return self.id

    def __str__(self):
        return self.id