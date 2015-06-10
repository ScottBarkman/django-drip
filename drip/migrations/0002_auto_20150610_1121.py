# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drip', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drip',
            name='base_model',
        ),
        migrations.RemoveField(
            model_name='drip',
            name='user_field',
        ),
    ]
