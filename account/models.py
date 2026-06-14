from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.conf import settings
from django.utils.crypto import get_random_string
from django.utils import timezone


class User(AbstractUser):
    STATUS_CHOICES = (
    ("student", "Student"),
    ("teacher", "Teacher"),
    ("admin", "Admin"),
)
    create_at = models.DateField(auto_now_add=True)
    is_user = models.CharField(max_length=50, choices=STATUS_CHOICES, default='student')

    def __str__(self):
        return self.username
    
class PasswordReset(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254)
    token = models.CharField(max_length=50, default=get_random_string(32), editable=False, unique=True)

    TOKEN_VALIDITY_PERIOD = timezone.timedelta(hours = 1)
    def is_valid(self):
        return timezone.now()<= self.creates_at + self.TOKEN_VALIDITY_PERIOD
    
    def send_reset_email(self):
        reset_link = f"http://127.0.0.1:8000/reset-password/{self.token}/"
        send_mail('Password Reset Request',
        f'reser your passsword: {reset_link}',
        settings.DEFAULT_FROM_EMAIL, [self.email], fail_silently=False)