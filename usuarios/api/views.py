from django.db.models import Q
from rest_framework import generics, mixins

from backend.permisos import AuthFirebaseUser
from usuarios.models import Usuario
from .serializers import UsuarioSerializer


class UsuariosView(generics.RetrieveUpdateAPIView):
    lookup_field = 'uid'
    serializer_class = UsuarioSerializer
    permission_classes = (AuthFirebaseUser,)

    def get_queryset(self):
        return Usuario.objects.all()


class UsuariosListView(generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = UsuarioSerializer
    # permission_classes = (AuthFirebaseUser,)

    def get_queryset(self):
        qs = Usuario.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(Q(nombre__icontains=query)).distinct()
        return qs


class UsuariosCreateView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = UsuarioSerializer

    def get_queryset(self):
        return None

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UsuariosSuscritosView(generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = UsuarioSerializer
    permission_classes = (AuthFirebaseUser,)

    def get_queryset(self):
        qs = Usuario.objects.all()
        query = self.request.GET.get('enfermedad')
        if query is not None:
            qs = qs.filter(Q(suscripcion__enfermedad__id=query))
        return qs
