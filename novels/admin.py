from django.contrib import admin
from novels.models import Description, Genero
# Register your models here.


class Authoradmin(admin.ModelAdmin):
    filter_horizontal = ("author", 'genero',)


admin.site.register(Genero)
admin.site.register(Description, Authoradmin)
