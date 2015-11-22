# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PollApp', '0004_auto_20151122_2255'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='isMultiSelect',
            field=models.BooleanField(default=False),
        ),
    ]
