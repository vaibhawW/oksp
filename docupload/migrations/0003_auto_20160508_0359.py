# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-07 22:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [('docupload', '0002_auto_20160505_0834'), ]

    operations = [
        migrations.AlterField(
            model_name='documentation',
            name='doc_file',
            field=models.FileField(upload_to='/Users/akash/oksp/media/'), ),
    ]
