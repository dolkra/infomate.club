# Generated by Django 2.2.8 on 2020-01-07 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='token',
            field=models.CharField(max_length=1024, unique=True),
        ),
    ]