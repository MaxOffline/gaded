# Generated by Django 2.2.7 on 2019-12-01 10:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('advertise', '0003_advertise_created_by'),
        ('notification', '0002_auto_20191201_1005'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscribe',
            name='category_name',
        ),
        migrations.AddField(
            model_name='subscribe',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subscribe', to='advertise.category'),
        ),
    ]