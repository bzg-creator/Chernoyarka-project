from django.db import models
from datetime import timedelta
# Create your models here.
class Zone(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='zones/', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    price_type = models.CharField(
        max_length=10,
        choices=[('day', 'Сутки'), ('hour', 'Часы')],
        default='day'
    )
    capacity = models.IntegerField(default=1)

    def __str__(self):
        return self.name

    def get_price(self, check_in, check_out, guests=1):
        duration_hours = (check_out - check_in).total_seconds() / 3600
        if self.price_type == 'day':
            price_total = self.price * (duration_hours / 24)
        else:
            price_total = self.price * duration_hours
        return price_total
