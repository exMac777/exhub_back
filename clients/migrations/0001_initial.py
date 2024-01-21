# Generated by Django 4.1.7 on 2023-04-16 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=200, null=True)),
                ('short_intro', models.TextField(blank=True, null=True)),
                ('profile_picture', models.ImageField(blank=True, default='images/experts/profile_photo/user-default.png', null=True, upload_to='images/clients/profile_photo')),
            ],
        ),
    ]
