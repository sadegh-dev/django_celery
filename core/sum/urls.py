from django.urls import path
from . import views

app_name = 'sum'

urlpatterns = [
    path('', views.home, name='home'),
]