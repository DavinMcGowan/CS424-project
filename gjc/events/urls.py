from django.urls import path

from . import views

urlpatterns = [
    path('event/id/<int:event_id>', views.event),
    path('eventlist', views.event_list),
]
