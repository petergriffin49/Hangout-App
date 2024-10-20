from django.views.generic import ListView, CreateView

# [add page screen]
def CreateSpotView(CreateView):

    model = Spot
    form_class = SpotForm
    template_name = "AddSpot.html"
    success_url = reverse_lazy("home")
