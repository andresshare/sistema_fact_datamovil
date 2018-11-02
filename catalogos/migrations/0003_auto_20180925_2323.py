# Generated by Django 2.1.1 on 2018-09-26 05:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogos', '0002_auto_20180925_2255'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubCategoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activo', models.BooleanField(default=True)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('descripcion', models.CharField(help_text='Descripción de la Sub Categoría', max_length=100)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogos.Categoria')),
            ],
            options={
                'verbose_name_plural': 'Sub Categorias',
            },
        ),
        migrations.AlterUniqueTogether(
            name='subcategoria',
            unique_together={('categoria', 'descripcion')},
        ),
    ]
