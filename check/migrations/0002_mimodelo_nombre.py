# Generated by Django 4.1.7 on 2023-04-01 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('check', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mimodelo',
            name='nombre',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
