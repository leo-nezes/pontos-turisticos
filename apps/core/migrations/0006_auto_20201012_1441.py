# Generated by Django 3.1.2 on 2020-10-12 17:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('enderecos', '0001_initial'),
        ('core', '0005_auto_20201010_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pontoturistico',
            name='enderecos',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='enderecos.endereco'),
        ),
    ]