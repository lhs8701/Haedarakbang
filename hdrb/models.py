from django.db import models


# Create your models here.
from django.utils import timezone


class Reservation(models.Model):
    # registrant 로그인 기능 구현 후 추가
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    num_of_people = models.IntegerField()
    allow_join = models.BooleanField(default=True)
    memo = models.TextField(null=True, blank=True)
