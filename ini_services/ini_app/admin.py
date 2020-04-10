from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Testimonial
from .models import Image

admin.site.site_header = 'INI Services'

class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'rating')
    list_filter = ('created_at',)

class ImageAdmin(admin.ModelAdmin):
    list_display = ('name', 'img')
    list_filter = ('created_at',)

admin.site.register(Testimonial, TestimonialAdmin)
admin.site.register(Image, ImageAdmin)
