# Generated by Django 4.2 on 2024-03-08 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_g', '0005_celular_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='celular',
            name='imagen',
            field=models.ImageField(null=True, upload_to='imagenes/'),
        ),
    ]