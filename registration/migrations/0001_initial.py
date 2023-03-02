# Generated by Django 4.1.4 on 2022-12-23 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('coursecode', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('coursename', models.TextField(max_length=128)),
                ('coursedate', models.DateField(blank=True, null=True)),
            ],
        ),
    ]