# Generated by Django 4.0.5 on 2022-12-27 02:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0007_student_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='status',
        ),
    ]