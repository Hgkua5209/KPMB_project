# Generated by Django 4.1.4 on 2022-12-29 02:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('studentid', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('studentname', models.TextField(max_length=128)),
                ('studentphone', models.TextField(max_length=12)),
                ('studentemail', models.TextField(max_length=128)),
                ('studentgender', models.TextField(max_length=128)),
                ('coursecode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.course')),
            ],
        ),
    ]