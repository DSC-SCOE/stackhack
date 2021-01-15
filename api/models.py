from django.db import models
from django.contrib.auth.models import User


class empData(models.Model):
    eid = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    address = models.TextField(max_length=200)
    tenth_marks = models.PositiveIntegerField()
    tenth_cert = models.FileField()
    twelth_marks = models.PositiveIntegerField()
    twelth_cert = models.FileField()
    degree_marks = models.PositiveIntegerField()
    degree_cert = models.FileField()
    resume = models.FileField(blank=True)
    status = models.BooleanField(default=False)


EMP_ROLE = {
    (),
}


class empModel(models.Model):
    eid = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    role = models.TextField()
    team = models.TextField()
    salary = models.PositiveIntegerField()


class leaveModel(models.Model):
    eid = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    cur_date = models.DateField()
    from_date = models.DateField()
    to_date = models.DateField()
    reason = models.TextField(max_length=100)
    discription = models.TextField(max_length=1000)


A_CHOICES = {
    ("1", "present"),
    ("0", "absent"),
}


class attendanceModel(models.Model):
    date = models.DateField()
    eid = models.OneToOneField(User, on_delete=models.CASCADE)
    status = models.TextField(choices=A_CHOICES)
