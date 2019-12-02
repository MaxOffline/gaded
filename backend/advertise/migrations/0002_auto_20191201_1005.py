# Generated by Django 2.2.7 on 2019-12-01 10:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('advertise', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertise',
            name='reviewed_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='admin', related_query_name='admin', to=settings.AUTH_USER_MODEL, verbose_name='admin'),
        ),
        migrations.AlterUniqueTogether(
            name='category',
            unique_together={('name', 'parent')},
        ),
    ]
