# Generated by Django 2.2.3 on 2020-09-11 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_alumno'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
