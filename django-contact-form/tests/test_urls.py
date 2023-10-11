"""
URLConf for testing django-contact-form.

"""

from django.urls import path
from django.views.generic import TemplateView

from django_contact_form.forms import AkismetContactForm
from django_contact_form.views import ContactFormView

urlpatterns = [
    path("", ContactFormView.as_view(), name="django_contact_form"),
    path(
        "sent/",
        TemplateView.as_view(
            template_name="django_contact_form/contact_form_sent.html"
        ),
        name="django_contact_form_sent",
    ),
    path(
        "test_recipient_list/",
        ContactFormView.as_view(recipient_list=["recipient_list@example.com"]),
        name="test_recipient_list",
    ),
    path(
        "test_akismet_form/",
        ContactFormView.as_view(form_class=AkismetContactForm),
        name="test_akismet_form",
    ),
]
