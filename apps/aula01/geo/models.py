from django.db.models import Model, CharField, TextField, ForeignKey, CASCADE

# Create your models here.

class UF(Model):
    sigla = CharField("Sigla", max_length=2, null=False, blank=False, primary_key=True)
    codigo = CharField("Código", max_length=2, null=False, blank=False)
    nome  = CharField("Nome", max_length=255, null=False, blank=False)

    class Meta:
        verbose_name = "UF"
        verbose_name_plural = "UFs"

    def __str__(self):
        return self.sigla


class Municipio(Model):
    codigo = CharField("Código", max_length=7, null=False, blank=False)
    nome  = CharField("Nome", max_length=255, null=False, blank=False)
    uf  = ForeignKey(UF, null=False, blank=False, on_delete=CASCADE)

    class Meta:
        verbose_name = "Município"
        verbose_name_plural = "Municípios"

    def __str__(self):
        return "%s (%s)" % (self.nome, self.uf)


class Tipo(Model):
    tipo = CharField("Tipo", max_length=255, null=False, blank=False)

    def __str__(self):
        return self.tipo


class Programa(Model):
    programa = CharField("Tipo", max_length=255, null=False, blank=False)

    def __str__(self):
        return self.programa


class Edital(Model):
    tipo = ForeignKey(Tipo, null=False, blank=False, on_delete=CASCADE)
    programa = ForeignKey(Programa, null=False, blank=False, on_delete=CASCADE)
    numero = CharField("Número", max_length=255, null=False, blank=False)
    sigla = CharField("Sigla", max_length=255, null=False, blank=False)
    link = CharField("Link", max_length=255, null=False, blank=False)
    descricao = TextField("Sigla", null=False, blank=False)
    ano = CharField("Ano", max_length=4, null=False, blank=False)
    periodo = CharField("Período", max_length=1, null=False, blank=False)

    # class Meta:
    #     verbose_name = "Município"
    #     verbose_name_plural = "Municípios"

    def __str__(self):
        return "%s (%s)" % (self.tipo, self.programa, self.descricao, self.link, self.numero, self.sigla, self.ano, self.periodo)

