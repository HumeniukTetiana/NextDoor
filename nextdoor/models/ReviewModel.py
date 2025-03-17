from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from .UserModel import User

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review by {self.user.email} - {self.rating}/5'




