from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('detail/<int:event_pk>', views.event_detail, name='event_detail'),
]
