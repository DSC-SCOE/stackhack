# Generated by Django 3.1.4 on 2021-01-22 11:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('api', '0006_auto_20210122_1002'),
    ]

    operations = [
        migrations.CreateModel(
            name='empList',
            fields=[
                ('eid', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('date', models.DateField()),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='attendancemodel',
            name='status',
            field=models.TextField(choices=[('0', 'absent'), ('1', 'present')]),
        ),
    ]