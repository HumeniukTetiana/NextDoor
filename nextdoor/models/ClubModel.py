from django.db import models
from .InterestModel import Interest

class Club(models.Model):
    name = models.CharField(max_length=255)
    location = models.URLField()  # Посилання на Google Maps
    price = models.DecimalField(max_digits=10, decimal_places=2)
    min_age = models.IntegerField()
    max_age = models.IntegerField()
    general_info = models.TextField(blank=True, null=True)
    contact_info = models.CharField(max_length=255, blank=True, null=True)
    interests = models.ManyToManyField(Interest)

    def __str__(self):
        return self.name

    def average_rating(self):
        reviews = self.review_set.all()
        if reviews.exists():
            return sum(review.rating for review in reviews) / reviews.count()
        return "Відгуків ще немає"