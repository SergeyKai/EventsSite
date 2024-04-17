from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('sub/', views.sub, name='sub'),
    path('un_sub/', views.un_sub, name='un_sub'),
    path('detail/<int:event_pk>', views.event_detail, name='event_detail'),
]
