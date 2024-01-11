from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import ListView
from .models import HistoryConfiguration
from .forms import ConfigurationFormSet
from django.contrib import messages



class ConfigListView(ListView):
    model = HistoryConfiguration
    template_name = "historyconfiguration/historyconfiguration_list.html"
    context_object_name = "configurations"
    success_message = "Configuration is successfully updated"

    fields = ["enable"]

    def post(self, request, *args, **kwargs):
        for config in HistoryConfiguration.objects.all():
            checkbox_name = f"enable_{config.pk}"
            new_enable_value = checkbox_name in request.POST

            # Compare the new value with the current value
            if config.enable != new_enable_value:
                config.enable = new_enable_value
                config.save()
        messages.success(self.request, self.success_message)
        return redirect(reverse_lazy("historyconfiguration:historyconfiguration_list"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["formset"] = ConfigurationFormSet(
            queryset=HistoryConfiguration.objects.all(), prefix="config_set"
        )
        return context
