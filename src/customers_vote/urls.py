# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from customers_vote.views import VoteView

urlpatterns = patterns(
    'customers_vote.views',
    url(r'(?P<customer_pk>[0-9]+)/$', VoteView.as_view(), name='vote'),
)
