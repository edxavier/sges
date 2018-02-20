from rest_framework import pagination
from rest_framework.response import Response
import math


class OperationsPaginator(pagination.PageNumberPagination):
    page_size = 7
    display_page_controls = True
        
    def get_paginated_response(self, data):
        # Calcular total de paginas
        res = (math.ceil(float(self.page.paginator.count) / float(self.page_size)))
        return Response({'pages': int(res),
                         'records': self.page.paginator.count,
                         'current': self.page.number,
                         'next': self.get_next_link(),
                         'previous': self.get_previous_link(),
                         'results': data
                         })
