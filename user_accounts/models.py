from django.db import models
from django.contrib.auth.models import User

class ToiletRanking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # User who ranked
    toilet_name = models.CharField(max_length=255)  # Name of the toilet
    location = models.CharField(max_length=255, blank=True, null=True)  # Optional location
    rating = models.IntegerField()  # Rating from 1 to 5
    review = models.TextField(blank=True, null=True)  # Optional text review
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp

    class Meta:
        ordering = ['-created_at']  # Sort by latest rankings

    def __str__(self):
        return f"{self.toilet_name} - {self.rating}⭐ by {self.user.username}"

# Create your models here.
