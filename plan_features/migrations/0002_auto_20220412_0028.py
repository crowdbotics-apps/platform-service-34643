# Generated by Django 2.2.26 on 2022-04-12 00:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plan_features', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='planfeatures',
            old_name='plan_id',
            new_name='plan',
        ),
    ]