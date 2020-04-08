from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Testimonial
import os
import smtplib

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

# Create your views here.
def index(request): 

    all_reviews = Testimonial.objects.all().order_by("-created_at")

    last_three = []

    if len(all_reviews) > 3:
        for i in range(3):
            last_three.append(all_reviews[i])
        

    context = {
        "last_three": last_three
    }

    return render(request, "index.html", context)

def create_review(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        rating = request.POST.get('rating')
        message = request.POST.get('message')
        
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

        smtp.sendmail(EMAIL_ADDRESS, 'ini1services@gmail.com', msg)

    # return redirect("/")
    return HttpResponse()


def gallery(request):
    return render(request, "gallery.html")