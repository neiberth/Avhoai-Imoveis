# Autor:        Neiberth Lucena Moreira
# Rede Social:  neiberth
# versão:       1.0.01

from django.db import models
from django.urls import reverse_lazy

# Models:
# Corretor
# Imovel
# Tipo do Imovel
# Status
# Imagens

# _______ Corretor _______
class Corretor(models.Model):
    nome    = models.CharField(max_length=100, null=False)
    email   = models.EmailField(max_length=100, null=True)
    celular = models.CharField(max_length=20, null=False)
    telefone= models.CharField(max_length=20, null=True)
    CREA    = models.CharField(max_length=30, null=False)
    foto    = models.ImageField(upload_to='imagem/', null=True, blank=True)

    class Meta:
        ordering = ('nome', )

    def __str__(self):
        return self.nome


# _______ Imovel _______
class Imovel(models.Model):
    cidade          = models.CharField(max_length=50, null=True)
    bairro          = models.CharField(max_length=50, null=False)
    endereco        = models.CharField(max_length=30, null=True)
    cep             = models.CharField(max_length=20, null=True)
    complemento     = models.CharField(max_length=500, null=True)
    area_contruida  = models.DecimalField('Área Construida', max_digits=7, decimal_places=2, null=True)
    area_terreno    = models.DecimalField('Área do Terreno', max_digits=7, decimal_places=2, null=False)
    valor_imovel    = models.DecimalField('Valor do Imovel', max_digits=7, decimal_places=2, null=True)
    valor_aluguel   = models.DecimalField('Valor do Aluguel', max_digits=7, decimal_places=2, null=True)
    valor_iptu      = models.DecimalField('Valor do IPTU', max_digits=7, decimal_places=2, null=True)
    valor_condominio= models.DecimalField('Valor do Condominio', max_digits=7, decimal_places=2, null=True)
    num_quartos     = models.IntegerField('Número de Quartos', null=False)
    num_suites      = models.IntegerField('Número de Suites', null=False)
    num_banheiros   = models.IntegerField('Número de Banheiros', null=False)
    num_vagas       = models.IntegerField('Número de Vagas', null=False)
    destaques       = models.CharField(max_length=600, null=True)
    observacoes     = models.TextField(max_length=500, null=True)

    corretor        = models.ForeignKey(Corretor, on_delete=models.CASCADE)

    def __str__(self):
        return self.valor_imovel

# _______ Tipo do Imovel _______
class TipoImovel(models.Model):
    tipoImovel  = models.CharField(max_length=100, null=False)

    imovel      = models.ForeignKey(Imovel, on_delete=models.CASCADE)

    def __str__(self):
        return self.tipoImovel

# _______ Status _______
class Status(models.Model):
    statusImovel = models.CharField(max_length=200, null=False)

    imovel       = models.ForeignKey(Imovel, on_delete=models.CASCADE)

    def __str__(self):
        return self.statusImovel

# _______ Imagens _______
class imagem(models.Model):
    imagem = models.ImageField( upload_to='imagem', null=True, blank=True)

    imovel = models.ForeignKey(Imovel, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.imovel)
