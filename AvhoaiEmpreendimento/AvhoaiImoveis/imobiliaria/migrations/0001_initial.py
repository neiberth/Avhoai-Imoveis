# Generated by Django 3.2.9 on 2021-11-19 01:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Corretor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100, null=True)),
                ('celular', models.CharField(max_length=20)),
                ('telefone', models.CharField(max_length=20, null=True)),
                ('CREA', models.CharField(max_length=30)),
            ],
            options={
                'ordering': ('nome',),
            },
        ),
        migrations.CreateModel(
            name='Imovel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cidade', models.CharField(max_length=50, null=True)),
                ('bairro', models.CharField(max_length=50)),
                ('endereco', models.CharField(max_length=30, null=True)),
                ('cep', models.CharField(max_length=20, null=True)),
                ('complemento', models.CharField(max_length=500, null=True)),
                ('area_contruida', models.DecimalField(decimal_places=2, max_digits=7, null=True, verbose_name='Área Construida')),
                ('area_terreno', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Área do Terreno')),
                ('valor_imovel', models.DecimalField(decimal_places=2, max_digits=7, null=True, verbose_name='Valor do Imovel')),
                ('valor_aluguel', models.DecimalField(decimal_places=2, max_digits=7, null=True, verbose_name='Valor do Aluguel')),
                ('valor_iptu', models.DecimalField(decimal_places=2, max_digits=7, null=True, verbose_name='Valor do IPTU')),
                ('valor_condominio', models.DecimalField(decimal_places=2, max_digits=7, null=True, verbose_name='Valor do Condominio')),
                ('num_quartos', models.IntegerField(verbose_name='Número de Quartos')),
                ('num_suites', models.IntegerField(verbose_name='Número de Suites')),
                ('num_banheiros', models.IntegerField(verbose_name='Número de Banheiros')),
                ('num_vagas', models.IntegerField(verbose_name='Número de Vagas')),
                ('destaques', models.CharField(max_length=600, null=True)),
                ('observacoes', models.TextField(max_length=500, null=True)),
                ('corretor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imobiliaria.corretor')),
            ],
        ),
        migrations.CreateModel(
            name='TipoImovel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipoImovel', models.CharField(max_length=100)),
                ('imovel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imobiliaria.imovel')),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statusImovel', models.CharField(max_length=200)),
                ('imovel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imobiliaria.imovel')),
            ],
        ),
        migrations.CreateModel(
            name='imagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', models.ImageField(upload_to='', verbose_name='imagem')),
                ('imovel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imobiliaria.imovel')),
            ],
        ),
    ]
