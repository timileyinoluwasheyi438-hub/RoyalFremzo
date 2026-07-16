from django.contrib import admin
from .models import Room, Booking


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price_per_night', 'beds', 'baths', 'is_featured')
    list_filter = ('category', 'is_featured')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'room', 'check_in', 'check_out', 'created_at')
    list_filter = ('room',)
