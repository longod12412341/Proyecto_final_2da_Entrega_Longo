# Generated by Django 4.2 on 2024-03-13 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_remove_celularnuevo_estado_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='celularnuevo',
            name='estado',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
