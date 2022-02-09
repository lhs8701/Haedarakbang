from django import forms
from django.db.models import Q
from hdrb.models import Reservation


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

    def clean(self):
        start_time = self.cleaned_data.get('start_time')
        end_time = self.cleaned_data.get('end_time')
        allow_join = self.cleaned_data.get('allow_join')
        if start_time is not None and end_time is not None and allow_join is not None:
            reservation_list = Reservation.objects.all()
            reservation_set = Reservation.objects.filter(
                (Q(start_time__lte=start_time) & Q(end_time__gt=start_time))
                | (Q(start_time__lte=end_time) & Q(end_time__gt=end_time))
            )
            if end_time.__lt__(start_time):
                raise forms.ValidationError('예약 종료 시간은 시작 시간 이후여야 합니다.')

            if reservation_set and (not allow_join or not reservation_set.first().allow_join):
                raise forms.ValidationError("기존 예약과 충돌합니다.")
        return self.cleaned_data
