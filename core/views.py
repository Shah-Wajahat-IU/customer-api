from django.shortcuts import render
from .models import Customer, DataSheet, Document, Professions
from .serializers import CustomerSerializer, DataSheetSerializer, DocumentSerializer, ProfessionSerializer
from rest_framework import viewsets


# Create your views here.

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class ProfessionViewSet(viewsets.ModelViewSet):
    queryset=Professions.objects.all()
    serializer_class=ProfessionSerializer

class DataViewSet(viewsets.ModelViewSet):
    queryset=DataSheet.objects.all()
    serializer_class=DataSheetSerializer

class DocumentViewSet(viewsets.ModelViewSet):
    queryset=Document.objects.all()
    serializer_class=DocumentSerializer