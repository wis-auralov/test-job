# -*- coding: utf-8 -*-
from django.contrib import admin
from customers.models import Customer


class CustomerAdmin(admin.ModelAdmin):
    fields = ('first_name', 'last_name', 'birthday', 'age', 'avatar')
    list_display = ('first_name', 'last_name', 'birthday', 'age')
    search_fields = ('first_name', 'last_name')
    readonly_fields = ('age',)


admin.site.register(Customer, CustomerAdmin)