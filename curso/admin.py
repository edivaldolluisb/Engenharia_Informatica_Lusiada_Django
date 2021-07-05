from django.contrib import admin
from .models import Disciplina, Ano, Sala, AgendaTeste, AgendaEntrega, Calendario

# Register your models here.


class DisciplinaAdmin(admin.ModelAdmin):
    search_fields = ('nome', 'nome_curto',)


class AgendaTesteAdmin(admin.ModelAdmin):
    list_display = ('sala', 'disciplina', 'data',)


class AgendaEntregaAdmin(admin.ModelAdmin):
    list_display = ('sala', 'disciplina')


admin.site.register(Ano)
admin.site.register(Disciplina, DisciplinaAdmin)
admin.site.register(Sala)
admin.site.register(AgendaTeste, AgendaTesteAdmin)
admin.site.register(AgendaEntrega)
admin.site.register(Calendario)
