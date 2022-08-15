from django.shortcuts import render, redirect
from api.models import Reservation
from . import forms
from django.core import validators
# Create your views here.
def reservationList(request):
    reservations = Reservation.objects.order_by('date','hour').all()
    data = { 'reservations': reservations, 'title': 'Administrar reservaciones' }
    
    return render(request, 'app/admin.html', data)

def reservationAdd(request):
    form = forms.ReservationForm()
    if request.method == 'POST':
        form = forms.ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return reservationList(request)
    data = { 'form': form, 'title': 'Agregar reservación' }
    return render(request, 'app/form.html', data)

def reservationEdit(request, id):
    reservation = Reservation.objects.get(id=id)
    form = forms.ReservationForm(instance=reservation)
    
    if request.method == 'POST':
        form = forms.ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return reservationList(request)
    data = { 'form': form, 'title': 'Editar reservación' }
    return render(request, 'app/form.html', data)

def reservationDelete(request, id):
    reservation = Reservation.objects.get(id=id)
    reservation.delete()
    return redirect('/')