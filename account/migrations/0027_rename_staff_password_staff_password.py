# Generated by Django 5.0.1 on 2024-03-24 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0026_staff_staff_password'),
    ]

    operations = [
        migrations.RenameField(
            model_name='staff',
            old_name='staff_password',
            new_name='password',
        ),
    ]
