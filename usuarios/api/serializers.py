from rest_framework import serializers

from usuarios.models import Usuario


class UsuarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Usuario
        fields = ['id',
                  'uid',
                  'nombre',
                  'email',
                  'genero',
                  'edad',
                  'peso',
                  'altura',
                  'enfermedad'
                  ]
