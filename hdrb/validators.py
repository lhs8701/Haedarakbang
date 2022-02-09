from django.core.exceptions import ValidationError
from django.utils import timezone


def validate_start_time(value):
    """start time이 과거면 error 발생"""
    if value.__lt__(timezone.now()):
        raise ValidationError('예약 시작 시간은 과거일 수 없습니다.')


def validate_end_time(value):
    """end time이 과거면 error 발생"""
    if value.__lt__(timezone.now()):
        raise ValidationError('예약 종료 시간은 과거일 수 없습니다.')
