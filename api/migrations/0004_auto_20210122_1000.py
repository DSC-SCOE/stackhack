# Generated by Django 3.1.4 on 2021-01-22 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210113_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendancemodel',
            name='status',
            field=models.TextField(choices=[('0', 'absent'), ('1', 'present')]),
        ),
    ]
