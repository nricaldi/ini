from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Testimonial

admin.site.site_header = 'INI Services'

class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'rating')
    list_filter = ('created_at',)

admin.site.register(Testimonial, TestimonialAdmin)
