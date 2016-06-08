# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
from django.conf import settings


class Customer(models.Model):
    first_name = models.CharField(u'Имя', max_length=50)
    last_name = models.CharField(u'Фамилия', max_length=50)
    birthday = models.DateField(u'Дата рождения')
    avatar = models.ImageField(
        u'Фото', upload_to='customers/', null=True, blank=True
    )

    age = lambda self: timezone.now().year - self.birthday.year
    age.short_description = u'Возраст'
    age.admin_order_field = 'birthday'

    @property
    def get_avatar_url(self):
        return '%s%s' % (settings.MEDIA_URL, self.avatar)

    class Meta:
        verbose_name = u'Клиент'
        verbose_name_plural = u'Клиенты'

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)