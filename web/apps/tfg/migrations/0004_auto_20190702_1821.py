# Generated by Django 2.2.1 on 2019-07-02 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tfg', '0003_auto_20190625_1952'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['fechaEntrada'], 'verbose_name': 'News', 'verbose_name_plural': 'News'},
        ),
        migrations.AlterField(
            model_name='news',
            name='url',
            field=models.URLField(),
        ),
    ]
