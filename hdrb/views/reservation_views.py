from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from hdrb.forms import ReservationForm
from hdrb.models import Reservation


def reservation_create(request):
    """
    예약 정보 생성
    """
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hdrb:index')
    else:
        form = ReservationForm()
    context = {'form': form}
    return render(request, 'hdrb/reservation_form.html', context)
