import django.forms
from django import forms

from .models import Reservation


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['start_time', 'end_time', 'num_of_people', 'allow_join', 'memo']
        labels = {
            'start_time': '시작 시간',
            'end_time': '종료 시간',
            'num_of_people': '인원수',
            'allow_join': '합석 가능',
            'memo': 'MEMO',
        }
