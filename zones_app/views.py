from django.shortcuts import render
from rest_framework import generics
from .models import Zone
from .serializers import ZoneSerializer

# Create your views here.

class ZoneList(generics.ListCreateAPIView):
    queryset = Zone.objects.all()
    serializer_class = ZoneSerializer


class ZoneDetail(generics.RetrieveAPIView):
    queryset = Zone.objects.all()
    serializer_class = ZoneSerializer
