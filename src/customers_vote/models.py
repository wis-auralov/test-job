# -*- coding: utf-8 -*-
from django.core.validators import MaxValueValidator
from django.db import models
from customers.models import Customer


class CustomerVote(models.Model):
    customer = models.OneToOneField(Customer)
    count = models.PositiveSmallIntegerField(
        u'Количество голосов', validators=[MaxValueValidator(10)], default=0
    )

    class Meta:
        verbose_name = u'Голос'
        verbose_name_plural = u'Голоса'