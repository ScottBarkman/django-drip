# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import drip.utils


class Migration(migrations.Migration):

    dependencies = [
        ('drip', '0002_auto_20150610_1121'),
    ]

    operations = [
        migrations.AddField(
            model_name='drip',
            name='base_model',
            field=models.CharField(default=drip.utils.get_user_model, help_text=b'Base model to filter', max_length=255, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='drip',
            name='user_field',
            field=models.CharField(default=b'', help_text=b'User field on base model to use as user', max_length=255, blank=True),
            preserve_default=True,
        ),
    ]
