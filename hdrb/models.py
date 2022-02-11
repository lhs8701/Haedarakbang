from django.contrib.auth.models import User
from django.db import models
from django import forms
from django.utils import timezone
from .validators import validate_start_time, validate_end_time


class Reservation(models.Model):
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField(validators=[validate_start_time])
    end_time = models.DateTimeField(validators=[validate_end_time])
    num_of_people = models.IntegerField()
    allow_join = models.BooleanField()
    memo = models.TextField(null=True, blank=True)
