from django.conf import settings
from django.db import models


class Subscriptions(models.Model):
    "Generated Model"
    user_id = models.ForeignKey(
        "plans.Plans",
        on_delete=models.CASCADE,
        related_name="subscriptions_user_id",
    )
    plan_id = models.BigIntegerField()
    start_at = models.DateTimeField()
    end_at = models.DateTimeField()
    status = models.BigIntegerField()
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )


# Create your models here.
