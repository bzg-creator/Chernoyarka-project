from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import RoomBooking, ZoneBooking
from .serializers import RoomBookingSerializer, ZoneBookingSerializer
from datetime import timedelta
from django.core.mail import send_mail
from django.conf import settings

class RoomBookingView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RoomBookingSerializer(data=request.data)
        if serializer.is_valid():
            room = serializer.validated_data['room']
            check_in = serializer.validated_data['check_in']
            check_out = serializer.validated_data['check_out']

            # Проверка на пересечение дат
            overlapping_bookings = RoomBooking.objects.filter(
                room=room,
                check_in__lt=check_out,
                check_out__gt=check_in
            )

            if overlapping_bookings.exists():
                return Response(
                    {"error": "Эта комната уже забронирована на выбранные даты."},
                    status=400
                )

            serializer.save()
            send_mail(
                subject="Новое бронирование номера",
                message=f"Имя: {serializer.validated_data['name']}\n"
                        f"Email: {serializer.validated_data['email']}\n"
                        f"Даты: {serializer.validated_data['check_in']} — {serializer.validated_data['check_out']}",
                from_email=None,
                recipient_list=[serializer.validated_data['email']],
                fail_silently=True,
            )
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class ZoneBookingView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = ZoneBookingSerializer(data=request.data)
        if serializer.is_valid():
            zone = serializer.validated_data['zone']
            booking_date = serializer.validated_data['booking_date']

            # Проверка на пересечение дат
            overlapping_bookings = ZoneBooking.objects.filter(
                zone=zone,
                booking_date=booking_date
            )

            if overlapping_bookings.exists():
                return Response(
                    {"error": "Эта зона уже забронирована на выбранную дату."},
                    status=400
                )

            serializer.save()

            # Отправка email пользователю
            send_mail(
                subject="Подтверждение бронирования зоны",
                message=(
                    f"Здравствуйте, {serializer.validated_data['name']}!\n\n"
                    f"Вы успешно забронировали зону: {zone.name}\n"
                    f"Дата бронирования: {booking_date}.\n"
                    f"Мы скоро свяжемся с вами для подтверждения.\n\n"
                    f"Спасибо за бронирование!"
                ),
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[serializer.validated_data['email']],
                fail_silently=True,
            )

            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class RoomBookingListView(ListAPIView):
    queryset = RoomBooking.objects.all().order_by('-created_at')
    serializer_class = RoomBookingSerializer

class ZoneBookingListView(ListAPIView):
    queryset = ZoneBooking.objects.all().order_by('-created_at')
    serializer_class = ZoneBookingSerializer

class BookedDatesView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        bookings = RoomBooking.objects.all()
        room_dates = {}

        for booking in bookings:
            room_id = booking.room.id
            current_date = booking.check_in

            while current_date < booking.check_out:
                room_dates.setdefault(room_id, []).append(current_date.strftime('%Y-%m-%d'))
                current_date += timedelta(days=1)

        return Response(room_dates)