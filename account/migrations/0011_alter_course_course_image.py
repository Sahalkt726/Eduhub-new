# Generated by Django 5.0.1 on 2024-03-19 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_image',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
