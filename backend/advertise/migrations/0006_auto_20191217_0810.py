# Generated by Django 2.2.7 on 2019-12-17 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertise', '0005_auto_20191217_0807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertise',
            name='since',
            field=models.DateField(auto_now=True),
        ),
    ]