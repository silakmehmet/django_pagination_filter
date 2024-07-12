from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination


class CustomPageNumberPagination(PageNumberPagination):
    page_size = 50
    page_query_param = 'page'


class CustomLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 2
    limit_query_param = 'adet'
    offset_query_param = 'baslangic'
