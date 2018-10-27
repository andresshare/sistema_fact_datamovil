# Generated by Django 2.1.2 on 2018-10-27 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(help_text='descripcion de la categoria', max_length=100, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Categorias',
            },
        ),
    ]