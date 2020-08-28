from django.urls import path

from .views import ParkedView, SubmitSuccessView

urlpatterns = [
    path("", ParkedView.as_view(), name="parked_landing"),
    path(
        "submitted", SubmitSuccessView.as_view(), name="parked_landing_submit_success"
    ),
]
