# Generated by Django 3.1.7 on 2021-02-24 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_auto_20210224_1044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='courseStudent',
            field=models.ManyToManyField(through='students.course_student', to='students.Student'),
        ),
    ]
