from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('sub/', views.sub, name='sub'),
    path('detail/<int:event_pk>', views.event_detail, name='event_detail'),
]
