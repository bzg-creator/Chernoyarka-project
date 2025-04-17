from django.urls import path
from . import views

urlpatterns = [
    path('', views.ZoneList.as_view(), name='zone-list'),
    path('<int:pk>/', views.ZoneDetail.as_view(), name='zone-detail'),
]
