from django.contrib import admin
from . models import Document,Customer,DataSheet,Professions
# Register your models here.

admin.site.register(Document)
admin.site.register(Customer)
admin.site.register(Professions)
admin.site.register(DataSheet)
