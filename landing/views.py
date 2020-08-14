from django.views.generic import TemplateView


class ParkedView(TemplateView):
    """
    Template view for landing page of the parked site.
    """
    http_method_names = ["get"]
    template_name = "landing/parked.html"
