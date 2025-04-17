from django.db import models
from zones_app.models import Zone
# Create your models here.
class Booking(models.Model):
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()
    guests = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=[('pending', 'Ожидает'), ('confirmed', 'Подтверждено'), ('cancelled', 'Отменено')],
        default='pending'
    )

    def __str__(self):
        return f"{self.name} - {self.zone.name} ({self.check_in.date()} ➜ {self.check_out.date()})"

    @staticmethod
    def check_availability(zone_id, check_in, check_out):
        overlapping_bookings = Booking.objects.filter(
            zone_id=zone_id,
            check_in__lt=check_out,
            check_out__gt=check_in,
            status__in=['pending', 'confirmed']  
        )
        return not overlapping_bookings.exists()
