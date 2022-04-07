from django.conf import settings
from django.db import models


class Apps(models.Model):
    "Generated Model"
    name = models.CharField(
        max_length=100,
    )
    description = models.TextField()
    is_active = models.BooleanField()
    user_id = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="apps_user_id",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        null=True,
        blank=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        null=True,
        blank=True,
    )
    subscription_id = models.ForeignKey(
        "subscriptions.Subscriptions",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="apps_subscription_id",
    )


# Create your models here.
