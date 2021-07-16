from rest_framework.test import APITestCase
from rest_framework.reverse import reverse as api_reverse
from rest_framework import status

from usuarios.models import Usuario


class UsuariosAPITestCase(APITestCase):
    def setUp(self):
        usuario = Usuario.objects.create(
            uid='',
            nombre='Usuario',
            email="test@test.com",
            genero='masculino',
            edad='26',
            peso='78',
            altura='1.78',
            enfermedad='accidente coronario')

    #########################################################################
    def test_single_usuario(self):
        usuarios_count = Usuario.objects.count()
        self.assertEqual(usuarios_count, 1)

    #########################################################################
    def test_get_usuarios_list_forbidden(self):
        data = {}
        url = api_reverse("")
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    #########################################################################
    def test_get_usuarios_list_with_user_ok(self):
        self.client.credentials(
            HTTP_AUTHORIZATION="")
        data = {}
        url = api_reverse("")
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    #########################################################################
    def test_post_usuarios_with_user_admin(self):
        self.client.credentials(
            HTTP_AUTHORIZATION="")

        data = {"uid": "ASFASFASFA",
                "nombre": "Test nombre",
                "email": "prueba@prueba.com",
                "edad": "45",
                "genero": "Masculino",
                "peso": "78",
                "altura": "1.78",
                "enfermedad": "hipertencion Test"}

        url = api_reverse("")
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    #########################################################################
    def test_put_usuarios_with_user_admin(self):
        self.client.credentials(
            HTTP_AUTHORIZATION="")

        usuarios = Usuario.objects.first()
        url = usuarios.get_api_url()

        data = {"uid": "FFFFFF",
                "nombre": "Test nombre",
                "email": "prueba@prueba.com",
                "genero": "Femenino",
                "edad": "56",
                "peso": "98",
                "altura": "1.69",
                "enfermedad": "riesgo cardiovascular Test"}

        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
