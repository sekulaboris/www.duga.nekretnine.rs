from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from . forms import ContactForm
from django.conf import settings
from django.core.mail import send_mail

def success_view(requst):
        return render (request, 'success.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']


            EmailMessage(
               'Contact Form Submission from {}'.format(name),
               message,
               'form-response@example.com', # Send from (your website)
               ['sekulaboris@yahoo.com'], # Send to (your admin email)
               [],
               reply_to=[email] # Email from the form to get back to
            ).send()

        return render(request,'contact:success_view')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


    