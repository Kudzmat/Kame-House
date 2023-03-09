from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.time_machine, name='time'),  # community

    path('inside', views.inside, name='inside'),  # inside
]
