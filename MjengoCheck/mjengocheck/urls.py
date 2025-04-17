from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='mjengocheck-home'),
    path('about/',views.about, name='mjengocheck-about'),
    path('ussd/',views.ussd_callback, name='mjengocheck-ussd')
]