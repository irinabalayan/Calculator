from django.urls import path
from . import views

urlpatterns = [
    path('calc/', views.calculate, name='calculate'),
]
