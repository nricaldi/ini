from django.db import models

# Create your models here.
class Testimonial(models.Model):
    name = models.CharField(max_length=255)
    message = models.TextField()
    rating = models.PositiveSmallIntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
