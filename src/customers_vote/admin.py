# -*- coding: utf-8 -*-
from django.contrib import admin
from customers_vote.models import CustomerVote


class CustomerVoteAdmin(admin.ModelAdmin):
    list_display = ('customer', 'count')

admin.site.register(CustomerVote, CustomerVoteAdmin)