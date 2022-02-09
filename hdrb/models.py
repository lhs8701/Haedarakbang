from django.db import models
from django import forms
from django.utils import timezone
from .validators import validate_start_time, validate_end_time


class Reservation(models.Model):
    # registrant 로그인 기능 구현 후 추가
    start_time = models.DateTimeField(validators=[validate_start_time])
    end_time = models.DateTimeField(validators=[validate_end_time])
    num_of_people = models.IntegerField()
    allow_join = models.BooleanField()
    memo = models.TextField(null=True, blank=True)
