# Generated by Django 5.0.4 on 2024-04-09 04:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0031_staff_profile_image_student_profile_image'),
        ('home', '0006_course_staff'),
        ('staff', '0019_delete_studymaterial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudyMaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('file', models.FileField(upload_to='study_materials/')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.student')),
            ],
        ),
    ]
