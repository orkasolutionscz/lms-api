from rest_framework import pagination
from rest_framework.response import Response
from collections import OrderedDict


class CustomLimitPagination(pagination.PageNumberPagination):
    page_size = 25
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('limit', self.page_size),
            ('count', self.page.paginator.count),
            ('page', self.page.number),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('results', data)
        ]))
