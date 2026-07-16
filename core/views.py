from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Room, Booking


def home(request):
    category = request.GET.get('category', 'all')
    rooms = Room.objects.all()
    if category != 'all':
        rooms = rooms.filter(category=category)

    context = {
        'rooms': rooms,
        'active_category': category,
        'categories': Room.CATEGORY_CHOICES,
    }
    return render(request, 'index.html',context)


def room_list(request):
    category = request.GET.get('category', 'all')
    rooms = Room.objects.all()
    if category != 'all':
        rooms = rooms.filter(category=category)

    context = {
        'rooms': rooms,
        'active_category': category,
        'categories': Room.CATEGORY_CHOICES,
    }
    return render(request, 'rooms.html', context)


def room_detail(request, slug):
    room = get_object_or_404(Room, slug=slug)
    related_rooms = Room.objects.exclude(slug=slug).filter(category=room.category)[:3]
    return render(request, 'room_detail.html', {'room': room, 'related_rooms': related_rooms})


def booking_create(request, room_slug):
    room = get_object_or_404(Room, slug=room_slug)

    if request.method == 'POST':
        Booking.objects.create(
            room=room,
            full_name=request.POST.get('full_name', ''),
            email=request.POST.get('email', ''),
            phone=request.POST.get('phone', ''),
            check_in=request.POST.get('check_in'),
            check_out=request.POST.get('check_out'),
            guests=request.POST.get('guests', 1),
            notes=request.POST.get('notes', ''),
        )
        messages.success(request, "Your reservation request has been received. We'll confirm shortly.")
        return redirect('room_detail', slug=room.slug)

    return render(request, 'booking.html', {'room': room})