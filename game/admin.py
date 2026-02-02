from django.contrib import admin
from game.models import Characters, Novel_game, Scenes, Dialogue, Choice
# Register your models here.


class ConfAdmin(admin.ModelAdmin):
    # Aqui van los campos del modelo a filtrar. NO el nombre de la clase
    filter_horizontal = ('character', )


admin.site.register(Characters)
admin.site.register(Novel_game, ConfAdmin)
admin.site.register(Scenes)
admin.site.register(Dialogue)
admin.site.register(Choice)
