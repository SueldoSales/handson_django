from django.contrib.admin import ModelAdmin, register
from .models import UF, Municipio, Edital, Programa, Tipo


@register(UF)
class UFAdmin(ModelAdmin):
    list_display = ('sigla', 'nome', 'codigo')


@register(Municipio)
class MunicipioAdmin(ModelAdmin):
    list_display = ('codigo', 'uf', 'nome')
    list_editable = ('uf', 'nome')
    list_filter = ('uf__nome', )
    search_fields = ('nome', 'codigo')

@register(Tipo)
class TipoAdmin(ModelAdmin):
    list_display = ('tipo',)


@register(Programa)
class ProgramaAdmin(ModelAdmin):
    list_display = ('programa',)


@register(Edital)
class TipoAdmin(ModelAdmin):
    list_display = ('tipo', 'programa', 'numero', 'sigla', 'link', 'descricao', 'ano', 'periodo', )