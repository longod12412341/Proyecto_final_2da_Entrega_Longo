# Generated by Django 4.2 on 2024-03-12 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='celularnuevo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('modelo', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('telefono', models.CharField(max_length=20)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=20, null=True)),
                ('estado', models.CharField(max_length=100, null=True)),
                ('imagen', models.ImageField(null=True, upload_to='celulares/')),
            ],
        ),
    ]