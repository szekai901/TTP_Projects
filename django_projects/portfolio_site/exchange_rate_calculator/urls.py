from exchange_rate_calculator import views
from django.urls import path

urlpatterns =[
    path('', views.index, name='index'),
]