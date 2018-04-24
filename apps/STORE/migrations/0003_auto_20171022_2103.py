# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-23 04:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('STORE', '0002_item_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='items',
        ),
        migrations.AddField(
            model_name='item',
            name='cart',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='items', to='STORE.Cart'),
            preserve_default=False,
        ),
    ]
