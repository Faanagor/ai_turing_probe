from django.contrib import admin
from .models import Cliente

class AdminCliente(admin.ModelAdmin):
    list_display = ["name_client", "email_client", "category", "country", "city", "user_created", "control_date", "is_active" ]
    list_filter = ["email_client", "category", "country", "city", "user_created", "control_date", "is_active" ]
    list_editable = ["email_client", "category", "country", "city", "control_date", "is_active" ]
    search_fields = ["name_client", "email_client", "category", "country", "city"]
    class Meta:
        model=Cliente

admin.site.register(Cliente, AdminCliente)
# Register your models here.
