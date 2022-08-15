from django.contrib import admin
from api.models import Reservation

# Register your models here.
class ReservationAdmin(admin.ModelAdmin):
    list_display = ["id", "reserverName", "phoneNumber", "date", "hour", "diners", "state", "observations"]
admin.site.register(Reservation, ReservationAdmin)