# Generated by Django 2.2.26 on 2022-04-11 11:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriptions',
            name='plan_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscriptions_plan_id', to='plans.Plans'),
        ),
        migrations.AlterField(
            model_name='subscriptions',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscriptions_user_id', to=settings.AUTH_USER_MODEL),
        ),
    ]