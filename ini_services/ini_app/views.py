from django.shortcuts import render, redirect
from .models import *
import os
import smtplib

# EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
# EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')
EMAIL_ADDRESS = 'nricaldi.nr@gmail.com'
EMAIL_PASSWORD = 'ipxmcaozywksjklc'


# Create your views here.
def index(request): 
    context = {
        "all_testimonials": Testimonial.objects.all().order_by("created_at")
    }

    return render(request, "index.html", context)

def leave_review(request, method="POST"):
    new_review = Testimonial.objects.create(name=request.POST['name'], message=request.POST['message'], rating=request.POST['rating'])
    # print('success')
    return redirect("/")

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

    return redirect("/")