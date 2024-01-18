from django.contrib import admin

from proyectoapp.models import (
    Socios,
    Libros,
    Avatar
)

admin.site.register(Socios)
admin.site.register(Libros)
admin.site.register(Avatar)


