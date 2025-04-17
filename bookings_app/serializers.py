from rest_framework import serializers
from .models import Booking
from django.utils import timezone

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
    def validate(self, data):
        check_in = data['check_in']
        check_out = data['check_out']
        zone = data['zone']

        if check_in < timezone.now() or check_out < timezone.now():
            raise serializers.ValidationError("Бронирование возможно только на будущее время.")

        if check_in >= check_out:
            raise serializers.ValidationError("Дата и время выезда должны быть позже заезда.")

        overlapping_bookings = Booking.objects.filter(
            zone=zone,
            check_out__gt=check_in,
            check_in__lt=check_out
        )

        if overlapping_bookings.exists():
            raise serializers.ValidationError("Эта зона уже забронирована на выбранное время.")

        return data