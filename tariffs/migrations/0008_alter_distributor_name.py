# Generated by Django 4.1 on 2023-03-22 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tariffs', '0007_alter_distributor_cnpj_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='distributor',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]