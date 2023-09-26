from django.urls import path
from . import views

app_name='contact'

urlpatterns = [
    path('', views.contact_view, name='contact_view'),
    path('uspesno-ste-poslali-poruku/', views.success_view, name='success_view')
]