# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.views.generic import View
from customers.models import Customer
from customers.tasks import queryset_to_xlsx_response


class CustomerExcelView(View):
    def get(self, request, *args, **kwargs):
        queryset = Customer.objects.all()
        response = self.get_excel_response(queryset)

        return response

    def get_excel_response(self, query_set):
        model_name = query_set.model._meta.model_name
        ct = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        response = HttpResponse(content_type=ct)
        file_type = 'attachment; filename="%s.xlsx"' % model_name
        response['Content-Disposition'] = file_type

        task = queryset_to_xlsx_response.delay(query_set, response)
        while not task.ready():
            # Ждём пока завершится задача. Блокирует поток, для продакшена
            # нужно было бы возвращать id задачи, а потом аяксом проверять
            # периодически завершилась ли задача и брать результат.
            pass

        return task.result