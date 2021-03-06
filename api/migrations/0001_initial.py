# Generated by Django 3.1.4 on 2021-01-13 09:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='empData',
            fields=[
                ('eid', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('address', models.TextField(max_length=200)),
                ('tenth_marks', models.PositiveIntegerField()),
                ('tenth_cert', models.FileField(upload_to='')),
                ('twelth_marks', models.PositiveIntegerField()),
                ('twelth_cert', models.FileField(upload_to='')),
                ('degree_marks', models.PositiveIntegerField()),
                ('degree_cert', models.FileField(upload_to='')),
                ('resume', models.FileField(blank=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='empModel',
            fields=[
                ('eid', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('role', models.TextField()),
                ('team', models.TextField()),
                ('salary', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='leaveModel',
            fields=[
                ('eid', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('cur_date', models.DateField()),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('reason', models.TextField(max_length=100)),
                ('discription', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='attendanceModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('status', models.TextField(choices=[('1', 'present'), ('0', 'absent')])),
                ('eid', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
