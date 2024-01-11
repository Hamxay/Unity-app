from django.urls import reverse_lazy
from django.views.generic import TemplateView, UpdateView, ListView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Notification

from django.contrib.auth import get_user_model

User = get_user_model()


class DashboardView(LoginRequiredMixin, TemplateView):
    pass

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["notification"] = Notification.objects.all()
        context["tips"] = Notification.objects.filter(type=3)
        context["warning"] = Notification.objects.filter(type=2)
        return context


class ProfileUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = User
    fields = [
        "first_name",
        "last_name",
        "photo",
        "mobile",
        "address",
        "city",
        "state",
        "country",
        "zip_code",
    ]
    template_name = "dashboards/profile.html"
    success_url = reverse_lazy("report:report_list")
    success_message = "Profile has been updated successfully."

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["notification"] = Notification.objects.all()
        context["tips"] = Notification.objects.filter(type=3)
        context["warning"] = Notification.objects.filter(type=2)
        return context


dashboard_view = DashboardView.as_view(template_name="dashboards/index.html")


class NotificationListView(ListView):
    """Show the list of teams for role admin in the frontend"""

    model = Notification
    paginate_by = 10
    template_name = "dashboards/notification_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["notification"] = Notification.objects.all()
        context["tips"] = Notification.objects.filter(type=3)
        context["warning"] = Notification.objects.filter(type=2)
        return context


class NotificationDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    """Delete the email from unsubscribe list"""

    model = Notification
    success_url = reverse_lazy("dashboards:notification_list")
    success_message = "Record was deleted successfully"

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(NotificationDeleteView, self).delete(request, *args, **kwargs)
