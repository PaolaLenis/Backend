from django.shortcuts import render
from rest_framework import viewsets
from .models import *

# Create your views here.
class EnfermedadViewSite(viewsets.ModelViewSet):
    	queryset=Enfermedad.objects.all()
	#serializer_class=EnfermedadSerializer