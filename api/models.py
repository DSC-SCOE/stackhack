from django.db import models
from django.contrib.auth.models import User

class empData(models.Model):
    eid = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True),
    tenth_marks = models.PositiveIntegerField()
    tenth_cert = models.FileField()
    twelth_marks = models.PositiveIntegerField()
    twelth_cert = models.FileField()
    degree_marks = models.PositiveIntegerField()
    degree_cert = models.FileField()
    resume = models.FileField(blank=True)


class leaveModel(models.Model):
    eid = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True),
    cur_date = models.DateField()
    from_date = models.DateField()
    to_date = models.DateField()
    readon = models.TextField()