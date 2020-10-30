from django.db import models
from django.utils import timezone

# Create your models here.
class Cliente(models.Model):
    TECHNOLOGY = 'TEC'
    HEALTH = 'HEA'
    MINING_OIL_GAS = 'MOG'
    FINANCIAL = 'FIN'
    FOOD = 'FOO'
    TRANSPORT = 'TRA'
    CATEGORY_CHOICES = [
        (TECHNOLOGY, 'Tecnología'),
        (HEALTH, 'Salud'),
        (MINING_OIL_GAS, 'Minería, petróleo y gas'),
        (FINANCIAL, 'Financiero'),
        (FOOD, 'Alimento'),
        (TRANSPORT, 'Tranporte'),
    ]
    id_client    = models.IntegerField(primary_key=True)
    name_client = models.CharField(verbose_name="Nombre", max_length=50, null=False, blank=False)
    country = models.CharField(verbose_name="Pais", max_length=50, null=False, blank=False)
    city = models.CharField(verbose_name="Ciudad", max_length=50, null=False, blank=False)
    category = models.CharField(verbose_name="Categoría", choices=CATEGORY_CHOICES, max_length=20, default=TECHNOLOGY)
    user_created = models.DateTimeField(verbose_name="Fecha de Creación", default=timezone.now)
    email_client = models.EmailField(verbose_name="e-mail", max_length=60, null=False, blank=False, unique=True )
    is_active = models.BooleanField(verbose_name="Estado Activo")    
    control_date = models.DateTimeField(verbose_name="Fecha Contrato", blank=True, null=True)

    class Meta: 
        ordering = ["name_client", "category", "country", "city", "user_created" ]

    def __str__(self):
        return self.name_client