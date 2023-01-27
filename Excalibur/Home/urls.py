from django.contrib import admin
from django.urls import path
from Home import views
urlpatterns = [
    path("",views.index, name = 'home'),
    path("about",views.about, name = 'about'),
    path("advice",views.advice, name='advice'),
    path("learn",views.learn, name='learn'),
    path("returns",views.returns, name='returns'),
    path("contact",views.contact, name='contact'),
    path("prices",views.prices, name='prices'), 
    path("forex",views.forex, name='forex'), 

]