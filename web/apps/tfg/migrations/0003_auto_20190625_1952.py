# Generated by Django 2.2.1 on 2019-06-25 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tfg', '0002_auto_20190625_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='url',
            field=models.CharField(max_length=2000),
        ),
    ]
