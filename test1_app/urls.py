from django.urls import path
from test1_app import views


urlpatterns = [
    path('', views.help, name='help'),
    ]
