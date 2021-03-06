# Generated by Django 3.1.4 on 2021-01-13 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210113_1339'),
    ]

    operations = [
        migrations.AddField(
            model_name='empdata',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='attendancemodel',
            name='status',
            field=models.TextField(choices=[('1', 'present'), ('0', 'absent')]),
        ),
    ]
