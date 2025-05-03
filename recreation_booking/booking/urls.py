from django.urls import path
from .views import RoomBookingView, ZoneBookingView, RoomBookingListView, ZoneBookingListView, BookedDatesView

urlpatterns = [
    path('rooms/book/', RoomBookingView.as_view()),
    path('zones/book/', ZoneBookingView.as_view()),
    path('rooms/bookings/', RoomBookingListView.as_view()),
    path('zones/bookings/', ZoneBookingListView.as_view()),
    path('booked-dates/', BookedDatesView.as_view(), name='booked-dates'),
]
