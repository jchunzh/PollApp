# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('text', models.CharField(max_length=500)),
                ('isSelected', models.BooleanField(default=False)),
                ('votes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('question', models.CharField(max_length=1000)),
                ('isMultiSelect', models.BooleanField(default=False)),
                ('uniqueId', models.CharField(max_length=24, default=None)),
            ],
        ),
        migrations.AddField(
            model_name='choice',
            name='poll',
            field=models.ForeignKey(related_name='choices', to='PollApp.Poll'),
        ),
    ]
