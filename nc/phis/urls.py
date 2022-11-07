from django.contrib import admin
from django.urls import path
from phis import views
urlpatterns = [
    path('',views.succ, name='success'),
    path('Account/Login',views.login, name='login'),
]
