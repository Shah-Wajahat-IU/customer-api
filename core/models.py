from django.db import models

# Create your models here.

class Professions(models.Model):
    des=models.CharField(max_length=50)

class DataSheet(models.Model):
    des=models.CharField(max_length=50)
    historical_data=models.TextField()


class Customer(models.Model):
    name=models.CharField( max_length=50)
    address=models.CharField(max_length=60)
    prof=models.ManyToManyField(Professions)
    data_sheet=models.OneToOneField(DataSheet, on_delete=models.CASCADE)


    def __str__(self):
        return  self.name


class Document(models.Model):
    PP="PP"
    ID="ID"
    OT="OT"

    DOCT_TYPE=(
        (PP,"Passport"),
        (ID,"Identy card"),
        (OT,"Others")
    )
    
    dtype= models.CharField(choices=DOCT_TYPE,max_length=2)
    doc_number=models.CharField(max_length=50)
    name = models.ForeignKey(Customer, on_delete=models.CASCADE)


    def __str__(self):
        return self.doc_number
   


