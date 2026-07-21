from cloudinary.models import CloudinaryField
from django.db import models
from django.urls import reverse


class Room(models.Model):
    CATEGORY_CHOICES = [
        ('suite', 'Suite'),
        ('penthouse', 'Penthouse'),
        ('studio', 'Studio'),
    ]

    name = models.CharField(max_length=120)
    slug = models.SlugField(max_length=140, unique=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    location = models.CharField(max_length=150, blank=True)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    beds = models.PositiveSmallIntegerField(default=1)
    baths = models.PositiveSmallIntegerField(default=1)
    sqft = models.PositiveIntegerField(default=0)
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=4.8)
    short_description = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    image =CloudinaryField('images', blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-is_featured', 'name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('core:room_detail', kwargs={'slug': self.slug})


class Booking(models.Model):
    amount =models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='bookings')
    full_name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=30, blank=True)
    check_in = models.DateField()
    check_out = models.DateField()
    guests = models.PositiveSmallIntegerField(default=1)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} — {self.room.name}"