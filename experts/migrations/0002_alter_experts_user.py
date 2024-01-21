# Generated by Django 4.1.7 on 2023-04-26 10:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('experts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experts',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='expert', to=settings.AUTH_USER_MODEL),
        ),
    ]
