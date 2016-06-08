# -*- coding: utf-8 -*-
from django.http import JsonResponse
from django.views.generic import ListView, View
from django.db import transaction
from customers.models import Customer
from customers_vote.models import CustomerVote


class CustomerVoteListView(ListView):
    template_name = 'customers_vote/customer_list.html'

    def get_queryset(self):
        return Customer.objects.filter(avatar__gt=0)\
            .select_related('customervote')


class VoteView(View):
    @transaction.atomic
    def post(self, request, *args, **kwargs):
        customer = Customer.objects.get(pk=kwargs['customer_pk'])
        vote, created = CustomerVote.objects.select_for_update().get_or_create(
            customer=customer
        )

        if created or vote.count < 10:
            vote.count += 1
            vote.save()
            result = {'vote_active': True, 'vote_count': vote.count}
        else:
            result = {'vote_active': False, 'vote_count': vote.count}

        return JsonResponse(result)
