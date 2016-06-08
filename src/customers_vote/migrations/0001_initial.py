# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerVote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('count', models.PositiveSmallIntegerField(default=0, verbose_name='\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0433\u043e\u043b\u043e\u0441\u043e\u0432', validators=[django.core.validators.MaxValueValidator(10)])),
                ('customer', models.OneToOneField(to='customers.Customer')),
            ],
            options={
                'verbose_name': '\u0413\u043e\u043b\u043e\u0441',
                'verbose_name_plural': '\u0413\u043e\u043b\u043e\u0441\u0430',
            },
        ),
    ]
