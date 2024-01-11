from django.contrib.auth.models import Group
from allauth.account.signals import email_confirmed
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import User


@receiver(email_confirmed)
def email_confirmed_(request, email_address, **kwargs):
    user = User.objects.get(email=email_address.email)
    print("email confirmed", user.role)
    if user.role == User.Roles.SRP or user.role == User.Roles.SCHOOL:
        user.is_active = False

        user.save()


@receiver(post_save, sender=User)
def assign_group(sender, instance, created, **kwargs):
    """Assign the group to a user as per their role to manage permissions for a app"""

    instance.groups.clear()
    group = Group.objects.get(name=instance.get_role_display())
    instance.groups.add(group)


def populate_models(sender, **kwargs):
    """Create the default groups as per the roles defined in the user models"""
    for role in User.Roles:
        Group.objects.get_or_create(name=role.label)
