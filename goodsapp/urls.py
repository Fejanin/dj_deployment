from django.urls import path
from . import views


urlpatterns = [
    path('', views.goods, name='goods'),
    ]
