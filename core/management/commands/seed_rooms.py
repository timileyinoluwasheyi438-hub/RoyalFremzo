from django.core.management.base import BaseCommand
from django.utils.text import slugify
from core.models import Room


class Command(BaseCommand):
    help = "Seed sample rooms for Royal Frenzo"

    def handle(self, *args, **options):
        rooms = [
            {
                "name": "Royal Penthouse Suite", "category": "penthouse",
                "location": "Lagos Island, Top Floor", "price_per_night": 280000,
                "beds": 3, "baths": 2, "sqft": 1850, "rating": 4.9,
                "short_description": "Panoramic Lagos skyline views with private terrace.",
                "description": "Our signature penthouse spans the entire top floor, offering uninterrupted views of Lagos Island. Features a private terrace, walk-in dressing room, and a dedicated butler on call around the clock.",
                "is_featured": True,
            },
            {
                "name": "Deluxe Suite", "category": "suite",
                "location": "Victoria Island Wing", "price_per_night": 145000,
                "beds": 2, "baths": 1, "sqft": 950, "rating": 4.8,
                "short_description": "Spacious suite with a king bed and lounge area.",
                "description": "A generous suite blending comfort with quiet elegance — a king bed, separate lounge, and floor-to-ceiling windows overlooking the gardens.",
                "is_featured": True,
            },
            {
                "name": "Garden Studio", "category": "studio",
                "location": "Garden Wing, Ground Floor", "price_per_night": 85000,
                "beds": 1, "baths": 1, "sqft": 480, "rating": 4.6,
                "short_description": "Cosy studio opening onto the private gardens.",
                "description": "Compact and comfortable, the Garden Studio opens directly onto Royal Frenzo's private gardens — ideal for solo travellers and short stays.",
                "is_featured": True,
            },
            {
                "name": "Royal Penthouse Suite", "category": "penthouse",
                "location": "Lagos Island, Top Floor", "price_per_night": 280000,
                "beds": 3, "baths": 2, "sqft": 1850, "rating": 4.9,
                "short_description": "Panoramic Lagos skyline views with private terrace.",
                "description": "Our signature penthouse spans the entire top floor, offering uninterrupted views of Lagos Island. Features a private terrace, walk-in dressing room, and a dedicated butler on call around the clock.",
                "is_featured": True,
            },
            {
                "name": "Executive Suite", "category": "suite",
                "location": "Business Wing, 4th Floor", "price_per_night": 165000,
                "beds": 2, "baths": 2, "sqft": 1100, "rating": 4.7,
                "short_description": "Designed for the travelling executive.",
                "description": "A refined suite with a dedicated workspace, fast Wi-Fi, and access to the executive lounge and meeting rooms.",
            },
            {
                "name": "Sky Studio", "category": "studio",
                "location": "Lagos Island, 9th Floor", "price_per_night": 92000,
                "beds": 1, "baths": 1, "sqft": 510, "rating": 4.5,
                "short_description": "Elevated studio with city-facing balcony.",
                "description": "A bright, modern studio on the ninth floor with a private balcony overlooking the city lights.",
            },
            {
                "name": "Grand Penthouse", "category": "penthouse",
                "location": "Ikoyi Wing, Top Floor", "price_per_night": 340000,
                "beds": 4, "baths": 3, "sqft": 2200, "rating": 5.0,
                "short_description": "Our largest residence, built for families.",
                "description": "The Grand Penthouse is Royal Frenzo's most exclusive residence — four bedrooms, a private plunge pool, and a rooftop dining terrace.",
            },
            {
                "name": "Royal Penthouse Suite", "category": "penthouse",
                "location": "Lagos Island, Top Floor", "price_per_night": 280000,
                "beds": 3, "baths": 2, "sqft": 1850, "rating": 4.9,
                "short_description": "Panoramic Lagos skyline views with private terrace.",
                "description": "Our signature penthouse spans the entire top floor, offering uninterrupted views of Lagos Island. Features a private terrace, walk-in dressing room, and a dedicated butler on call around the clock.",
                "is_featured": True,
            },
        ]

        created = 0
        for r in rooms:
            slug = slugify(r["name"])
            _, was_created = Room.objects.update_or_create(
                slug=slug, defaults={**r, "slug": slug},
            )
            if was_created:
                created += 1

        self.stdout.write(self.style.SUCCESS(f"Seeded {len(rooms)} rooms ({created} newly created)."))
