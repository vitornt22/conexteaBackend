# Generated by Django 3.2.25 on 2025-06-24 21:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('parent', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='parent',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='school.user'),
            preserve_default=False,
        ),
    ]
