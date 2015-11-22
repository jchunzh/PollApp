# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PollApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('text', models.CharField(max_length=500)),
                ('isSelected', models.BooleanField(default=False)),
                ('votes', models.IntegerField()),
                ('poll', models.ForeignKey(to='PollApp.Poll')),
            ],
        ),
    ]
