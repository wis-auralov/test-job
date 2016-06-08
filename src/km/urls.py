# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.contrib.admin.views.decorators import staff_member_required
from customers.views import CustomerExcelView
from customers_vote.views import CustomerVoteListView

urlpatterns = patterns(
    '',
    url(
        r'^admin/customers/customer/xlsx/',
        staff_member_required(CustomerExcelView.as_view()),
        name='customers_to_xlsx'
    ),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin_tools/', include('admin_tools.urls')),
    url(
        r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}
    ),

    url(r'^$', CustomerVoteListView.as_view(), name='vote'),
    url(r'^customers/', include('customers.urls', namespace='customers')),
    url(r'^customers_vote/', include('customers_vote.urls',
                                     namespace='customers_vote')),
)
