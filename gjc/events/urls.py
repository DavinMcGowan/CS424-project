from django.urls import path

from . import views

urlpatterns = [
    path('event/id/<int:event_id>', views.event, name="event_profile"),
    path('eventlist', views.event_list),
    path('event/update/id/<int:event_id>', views.event_update, name="event_update"),
]
