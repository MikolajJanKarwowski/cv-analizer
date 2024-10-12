from django.contrib import admin 
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from core import models

# Register your models here.


class UserAdmin(BaseUserAdmin):
    """ Define the admin page for users """
    ordering = ["id"]
    list_display = ["username", "email", "is_active", "is_staff"]
    fieldsets = (
        (None, {"fields": ("username", "email", "password")}),
        ("Personal Info", {"fields": ("first_name", "last_name", "telefono")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "email", "password1", "password2", "is_active", "is_staff", "is_superuser")
        }),
    )

# Register the Usuario model with the custom UserAdmin
admin.site.register(models.Usuario, UserAdmin)
admin.site.register(models.CV)
admin.site.register(models.Experiencia)
admin.site.register(models.Educacion)
admin.site.register(models.Habilidad)
admin.site.register(models.Certificacion)
admin.site.register(models.Idioma)
admin.site.register(models.Proyecto)