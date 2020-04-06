# from django import forms
# from .models import Testimonial

# class ReviewForm(forms.ModelForm):
#     class Meta:
#         model = Testimonial
#         # exclude = ['author', 'updated', 'created', ]
#         fields = ['name', 'rating', 'message']
#         widgets = {
#             'name': forms.TextInput(attrs={
#                 'id': 'review-name', 
#                 'class': 'review-name',
#                 'required': True, 
#                 'placeholder': 'Put ur name'
#             }),
#             'rating': forms.IntegerField(attrs={
#                 'id': 'review-rating',
#                 'class': 'review-rating',
#                 'required': True,
#                 'max': 5
#             }),
#             'message': forms.TextInput(attrs={
#                 'id': 'review-message', 
#                 'class': 'review-rating',
#                 'required': True, 
#                 'placeholder': 'Say someting'
#             }),
#         }