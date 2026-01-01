from django.contrib import admin
from novels.models import Author, Description, Genero
# Register your models here.


class Authoradmin(admin.ModelAdmin):
    filter_horizontal = ("author", 'genero',)


admin.site.register(Author)
admin.site.register(Genero)
admin.site.register(Description, Authoradmin)
