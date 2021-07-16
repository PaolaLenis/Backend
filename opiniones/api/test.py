from rest_framework.test import APITestCase
from rest_framework.reverse import reverse as api_reverse
from rest_framework import status

from opiniones.models import Opinion
from usuarios.models import Usuario
from tags.models import Tag
class OpinionesAPITestCase(APITestCase):
    def setUp(self):
        usuario = Usuario.objects.create(
            uid='Dq2hAFrjjwTR0SeGrTpKm8jr9Eq1',
            nombre='Usuario',
            email="test@test.com",
            genero='Masculino',
            enfermedad ='miocardio'
            )

        tags = []
        tag = Tag.objects.create(nombre="Test - Tag")
        tags.append(tag)

        
        opinion = Opinion.objects.create(usuario=usuario
                                         )

    #########################################################################
    
    def test_single_tags(self):
        tags_count = Tag.objects.count()
        self.assertEqual(tags_count, 1)

    def test_single_usuario(self):
        usuario_count = Usuario.objects.count()
        self.assertEqual(usuario_count, 1)

    def test_single_opinion(self):
        opinion_count = Opinion.objects.count()
        self.assertEqual(opinion_count, 1)

    #########################################################################
    def test_get_opiniones_list_forbidden(self):
        data = {}
        url = api_reverse("api-opiniones:opínion-create")
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    #########################################################################
    def test_get_opiniones_list_with_user_ok(self):
        self.client.credentials(
            HTTP_AUTHORIZATION=()
        data = {""}
        url = api_reverse("api-opiniones:opínion-create")
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    #########################################################################
    def test_post_opiniones_with_user_admin(self):
        self.client.credentials(
            HTTP_AUTHORIZATION=)

        data = {}

        url = api_reverse("api-opiniones:opínion-create")
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    #########################################################################
    def test_put_opiniones_with_user_admin(self):
        self.client.credentials(
            HTTP_AUTHORIZATION="")

        opiniones = Opinion.objects.first()
        url = opiniones.get_api_url()

        data = {}

        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

