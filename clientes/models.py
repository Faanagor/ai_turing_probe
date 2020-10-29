from django.db import models
from django.utils import timezone

# Create your models here.
class Clientes(models.Model):
    id_cliente = models.IntegerField(primary_key=True)
    name_client = models.CharField(max_length=50, null=False, blank=False)
    country = models.CharField(max_length=50, null=False, blank=False)
    city = models.CharField(max_length=50, null=False, blank=False)
    category = models.CharField(max_length=50, null=False, blank=False)
    user_created = models.DateTimeField(default=timezone.now)
    email_client = models.EmailField(max_length=60, null=False, blank=False)
    is_active = models.BooleanField()    
    control_date = models.DateTimeField(blank=True, null=True)

    class Meta: 
        ordering = ["name_client", "category", "country", "city", "user_created", ]

    def __str__(self):
        return self.name_client