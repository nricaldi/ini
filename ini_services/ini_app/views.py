from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import *
import os
import smtplib
# import simplejson as json
# from .forms import ReviewForm

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

# Create your views here.
def index(request): 

    # review_form = ReviewForm()

    context = {
        "all_testimonials": Testimonial.objects.all().order_by("created_at"),
        # "form": review_form
    }

    return render(request, "index.html", context)

def create_review(request):
    
    errors = Testimonial.objects.testimonial_validator(request.POST)

    # if len(errors) > 0:
    #     # request.session['try'] = "register"
    #     for key, value in errors.items():
    #         messages.error(request, value)

    #     # for message in errors:
    #     #     print(message)
    #     return redirect("/")

    if request.method == 'POST':
        name = request.POST.get('name')
        rating = request.POST.get('rating')
        message = request.POST.get('message')

        response_data = {}
        
        review = Testimonial(name=name, rating=rating, message=message)
        review.save()

        return HttpResponse()
    else: 
        return HttpResponse()

def send_mail(request, method="POST"):

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        subject = 'INI SERVICES CONTACT FORM'
        body = f'Name: {name} \nEmail: {email} \nMessage: {message}'

        msg = f'Subject: {subject}\n\n{body}'

        smtp.sendmail(EMAIL_ADDRESS, 'nr.ricaldi@gmail.com', msg)

    # return redirect("/")
    return HttpResponse()