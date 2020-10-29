from django.db import models
from django.utils import timezone

# Create your models here.
class Clientes(models.Model):
    id_cliente = models.ForeignKey()
    country = models.charfield(max_length=50, blanck=True, null=True)
    city = models.charfield(max_length=50, blanck=True, null=True)
    category = models.charfield(max_length=50, blanck=True, null=True)
    user_created = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField()    
    control_date = models.DateTimeField(blank=True, null=True)