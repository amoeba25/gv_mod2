# Generated by Django 3.1.8 on 2022-06-03 08:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('leadapp', '0003_auto_20220603_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leads',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='username'),
        ),
        migrations.AlterField(
            model_name='leads',
            name='source',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
