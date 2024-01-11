from django.apps import AppConfig
from django.db.models.signals import post_migrate


class AccountsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "accounts"

    def ready(self):
        from accounts.signals import populate_models

        # Create default groups for permissions
        post_migrate.connect(populate_models, sender=self)
