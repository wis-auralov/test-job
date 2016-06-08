# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=50, verbose_name='\u0418\u043c\u044f')),
                ('last_name', models.CharField(max_length=50, verbose_name='\u0424\u0430\u043c\u0438\u043b\u0438\u044f')),
                ('birthday', models.DateField(verbose_name='\u0414\u0430\u0442\u0430 \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f')),
                ('avatar', models.ImageField(upload_to=b'customers/', null=True, verbose_name='\u0424\u043e\u0442\u043e', blank=True)),
            ],
            options={
                'verbose_name': '\u041a\u043b\u0438\u0435\u043d\u0442',
                'verbose_name_plural': '\u041a\u043b\u0438\u0435\u043d\u0442\u044b',
            },
        ),
    ]
