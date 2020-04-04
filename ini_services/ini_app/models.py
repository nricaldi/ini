from django.db import models

class Error_manager(models.Manager):
    def testimonial_validator(self, postData):
        errors = {}

    def email_validator(self, postData):
        errors = {}

# Create your models here.
class Testimonial(models.Model):
    name = models.CharField(max_length=255)
    message = models.TextField()
    rating = models.PositiveSmallIntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Email(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255) 
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)