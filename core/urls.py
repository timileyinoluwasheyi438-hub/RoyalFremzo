from django.urls import path, include
from django.contrib import admin
from . import views

app_name = 'core'


urlpatterns = [
    path('',views.home, name='home'),
    path('rooms/',views.room_list, name='room_list'),
    path('room/<slug:slug>/', views.room_detail, name='room_detail'),
    path('booking/create/<slug:room_slug>/',views.booking_create, name='booking_create')

]
