from django.urls import path

from .views import ParkedView

urlpatterns = [
    path("", ParkedView.as_view(), name="parked_landing"),
]
