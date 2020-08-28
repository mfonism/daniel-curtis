from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from .models import WantToSee


class ParkedView(CreateView):
    http_method_names = ["get", "post"]
    template_name = "landing/parked.html"
    model = WantToSee
    fields = ["fullname", "email", "message"]
    success_url = reverse_lazy("parked_landing_submit_success")


class SubmitSuccessView(TemplateView):
    http_method_names = ["get"]
    template_name = "landing/submit-success.html"
