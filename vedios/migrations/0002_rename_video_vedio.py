# Generated by Django 4.2.4 on 2023-09-17 10:55

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vedios', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Video',
            new_name='Vedio',
        ),
    ]