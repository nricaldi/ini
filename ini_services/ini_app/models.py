from django.db import models
import re

class Error_manager(models.Manager):
    def testimonial_validator(self, postData):
        errors = {}

        if(len(postData['name']) < 1 and len(postData['message']) < 1):
            errors['form'] = "Form cannot be empty"
            return errors
        else: 
            if len(postData['name']) < 2:
                errors['name'] = "Name should be at least 2 characters"
            if len(postData['message']) < 10:
                errors['message'] = "Message should be at least 10 characters"

        return errors
            


    def email_validator(self, postData):
        errors = {}

        if (len(postData['name']) < 1 and len(postData['email']) < 1 and len(postData['message']) < 1):
            errors['form'] = "Form cannot be empty"

        else: 
            if len(postData['name']) < 2:
                errors['name'] = "Name should be at least 2 characters"
            EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
            if not EMAIL_REGEX.match(postData['email']):
                errors["email"] = "Invalid Email Address"
            if len(postData['name']) < 10:
                errors['message'] = "Name should be at least 10 characters"
        return errors



# Create your models here.
class Testimonial(models.Model):
    name = models.CharField(max_length=255)
    message = models.TextField()
    rating = models.PositiveSmallIntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = Error_manager()

class Email(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255) 
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)