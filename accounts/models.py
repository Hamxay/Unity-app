# Create your models here.
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
from django_countries.fields import CountryField


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True


class UserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)


def user_directory_path(instance, filename):
    """User profile photo directory path
    file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    """

    return "users/user_{0}/{1}".format(instance.id, filename)


phone_regex = RegexValidator(
    regex=r"^\+?1?\d{9,15}$",
    message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.",
)


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model to add more fields"""

    # User roles
    class Roles(models.IntegerChoices):
        """Roles for user model"""

        ADMIN = 1

    email = models.EmailField(_("email address"), unique=True)
    first_name = models.CharField(_("First Name"), max_length=50, blank=True, null=True)
    last_name = models.CharField(_("Last Name"), max_length=50, blank=True, null=True)
    photo = models.ImageField(
        _("photo"), upload_to=user_directory_path, null=True, blank=True
    )

    mobile = models.CharField(
        _("mobile"),
        max_length=17,
        validators=[phone_regex],
        null=True,
        blank=True,
    )

    address = models.TextField(_("Address"), blank=True, null=True)
    city = models.CharField(_("City/Town"), max_length=50, blank=True, null=True)
    state = models.CharField(_("State/Province"), max_length=50, blank=True, null=True)
    country = CountryField(blank=True)
    zip_code = models.CharField(max_length=50, blank=True, null=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(_("date joined"), auto_now_add=True)
    role = models.PositiveSmallIntegerField(
        _("role"), choices=Roles.choices, default=Roles.ADMIN
    )
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True, editable=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return self.get_full_name()

    def get_full_name(self):
        return "{} {}".format(self.first_name, self.last_name)
