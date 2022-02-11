from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from hdrb.forms import ReservationForm


@login_required()
def reservation_create(request):
    """
    예약 정보 생성
    """
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.writer = request.user
            reservation.save()
            return redirect('hdrb:index')
    else:
        form = ReservationForm()
    context = {'form': form}
    return render(request, 'hdrb/reservation_form.html', context)
