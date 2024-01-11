from django import template
from dashboards.models import Notification

register = template.Library()


@register.simple_tag
def notification_count():
    return Notification.objects.all().count()


@register.inclusion_tag("partials/topbar_notifications.html")
def show_notifications():
    return {"notifications": Notification.objects.all()}


@register.inclusion_tag("partials/topbar_notification_tips.html")
def show_tips():
    return {"tips": Notification.objects.filter(type=Notification.Type.TIP)}


@register.inclusion_tag("partials/topbar_notification_warnings.html")
def show_warnings():
    return {"warnings": Notification.objects.filter(type=Notification.Type.WARNING)}
