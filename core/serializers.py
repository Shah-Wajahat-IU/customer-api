from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from . models import Customer, DataSheet, Document, Professions

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id','name', 'address', 'prof', 'data_sheet']

class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Professions
        fields=['id','des']

class DataSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model=DataSheet
        fields=['id','des','historical_data']

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Document
        fields=['id','dtype','doc_number','name']