from django.views.generic import CreateView

from .models import WantToSee


class ParkedView(CreateView):
    """
    Template view for landing page of the parked site.
    """

    http_method_names = ["get", "post"]
    template_name = "landing/parked.html"
    model = WantToSee
    fields = ["fullname", "email", "message"]
    success_url = "/"
