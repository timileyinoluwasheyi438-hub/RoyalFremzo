import requests
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
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
    return render(request, 'index.html', context)


def room_detail(request, slug):
    room = get_object_or_404(Room, slug=slug)
    related_rooms = Room.objects.exclude(slug=slug).filter(category=room.category)[:3]
    return render(request, 'room_detail.html', {'room': room, 'related_rooms': related_rooms})

def booking_create(request, slug):
    room = get_object_or_404(Room, slug=slug)

    if request.method == 'POST':
        booking = Booking.objects.create(
            room=room,
            full_name=request.POST.get('full_name', ''),
            email=request.POST.get('email', ''),
            phone=request.POST.get('phone', ''),
            check_in=request.POST.get('check_in'),
            check_out=request.POST.get('check_out'),
            guests=request.POST.get('guests', 1),
            notes=request.POST.get('notes', ''),
            amount=room.price_per_night,
           
        )

        send_mail(
            subject=f'✅ New Booking: {booking.room.name}',
            message=(
                f'A new reservation has been made.\n\n'
                f'Room: {booking.room.name}\n'
                f'Guest: {booking.full_name}\n'
                f'Email: {booking.email}\n'
                f'Phone: {booking.phone}\n'
                f'Check-in: {booking.check_in}\n'
                f'Check-out: {booking.check_out}\n'
                f'Guests: {booking.guests}\n'
                f'Amount: ₦{booking.amount}\n'
            ),
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.ADMIN_EMAIL,booking.email],
            fail_silently=False,
        )

        return render(request, 'payment_success.html', {'booking': booking})

    return render(request, 'booking.html', {'room': room})

def splash(request):
    return render(request, 'splash.html')


def payment_callback(request):
    reference = request.GET.get('reference')

    response = requests.get(
        f'https://api.paystack.co/transaction/verify/{reference}',
        headers={'Authorization': f'Bearer {settings.PAYSTACK_SECRET_KEY}'},
    )
    data = response.json()

    if data.get('status') and data['data']['status'] == 'success':
        booking = get_object_or_404(Booking, paystack_reference=reference)
        booking.is_paid = True
        booking.save()

        send_mail(
            subject=f'✅ Paid Booking: {booking.room.name}',
            message=(
                f'Payment confirmed for a new reservation.\n\n'
                f'Room: {booking.room.name}\n'
                f'Guest: {booking.full_name}\n'
                f'Email: {booking.email}\n'
                f'Phone: {booking.phone}\n'
                f'Check-in: {booking.check_in}\n'
                f'Check-out: {booking.check_out}\n'
                f'Guests: {booking.guests}\n'
                f'Amount Paid: ₦{booking.amount}\n'
                f'Reference: {booking.paystack_reference}\n'
            ),
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.ADMIN_EMAIL],
            fail_silently=True,
        )

        return render(request, 'payment_success.html', {'booking': booking})

    messages.error(request, "Payment could not be verified. Please contact us if you were charged.")
    return redirect('core:home')
