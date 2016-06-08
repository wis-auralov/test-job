# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from admin_tools.dashboard import modules, Dashboard
from admin_tools.utils import get_admin_site_name


class KmDashboard(Dashboard):
    """
    Custom index dashboard for src.
    """
    def init_with_context(self, context):
        site_name = get_admin_site_name(context)
        # append a link list module for "quick links"
        self.children.append(modules.LinkList(
            _('Quick links'),
            layout='inline',
            children=[
                {
                    'title': u'Выгрузить клиентов в excel',
                    'url': 'customers/customer/xlsx/',
                },
            ]
        ))

        # append an app list module for "Applications"
        self.children.append(modules.AppList(
            _('Applications'),
            exclude=('django.contrib.*',),
        ))

        # append an app list module for "Administration"
        self.children.append(modules.AppList(
            _('Administration'),
            models=('django.contrib.*',),
        ))

        # append a recent actions module
        self.children.append(modules.RecentActions(_('Recent Actions'), 5))