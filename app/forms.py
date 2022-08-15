from datetime import datetime
from django import forms
from api.models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'
        labels = {
            'id': 'Identificador',
            'reserverName': 'Reservada por',
            'phoneNumber': 'Número de teléfono',
            'date': 'Fecha reserva',
            'hour': 'Hora reserva',
            'diners': 'Cantidad de comensales',
            'state': 'Estado',
            'observations': 'Observaciones'
        }
        widgets = {
            'id': forms.TextInput(attrs={'type': 'number', 'class': 'form-control'}),
            'reserverName': forms.TextInput(attrs={'type': 'teet', 'class': 'form-control'}),
            'phoneNumber': forms.TextInput(attrs={'type': 'tel', 'class': 'form-control'}),
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}, format='%Y-%m-%d'),
            'hour': forms.DateInput(attrs={'type': 'time', 'class': 'form-control'}, format='%H:%M'),
            'diners': forms.TextInput(attrs={'type': 'number', 'class': 'form-control', 'min': '1', 'max': '15'}),
            'state': forms.Select(attrs={'class': 'form-control'}),
            'observations': forms.Textarea(attrs={'class': 'form-control'})
        }
        
        def clean(self):
            cleaned_data = super(ReservationForm, self).clean()
            my_date = cleaned_data.get('date')
            my_time = cleaned_data.get('hour')
            if my_date and my_time:
                my_date_time = (my_date + ' ' + my_time + ':00')
                my_date_time = datetime.strptime(my_date_time, '%Y-%m-%d %H:%M:%S')
                if(datetime.now() > my_date_time):
                    self.add_error('date', 'La fecha y hora de la reserva no pueden ser pasadas')                    
                    raise forms.ValidationError('La fecha y hora de la reserva no puede ser anterior a la fecha y hora actual')   
                    return cleaned_data
        

