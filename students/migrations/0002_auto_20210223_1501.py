# Generated by Django 3.1.7 on 2021-02-23 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='courseCredit',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='score',
            name='scoreCredit',
            field=models.CharField(max_length=20),
        ),
    ]
