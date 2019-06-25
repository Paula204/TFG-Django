# Generated by Django 2.2.1 on 2019-06-25 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tfg', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='cabecera',
        ),
        migrations.RemoveField(
            model_name='news',
            name='cuerpo',
        ),
        migrations.AddField(
            model_name='news',
            name='fechaEntrada',
            field=models.DateField(auto_now=True, verbose_name='Fecha de creación'),
        ),
        migrations.AlterField(
            model_name='news',
            name='esFi',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='news',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='news',
            name='url',
            field=models.URLField(),
        ),
    ]
