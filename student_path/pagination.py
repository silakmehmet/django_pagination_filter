from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination


class CustomPageNumberPagination(PageNumberPagination):
    page_size = 50
    page_query_param = 'page'


class CustomLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 2
    limit_query_param = 'adet'
    offset_query_param = 'baslangic'


class CustomCursorPagination(CursorPagination):
    cursor_query_param = "cursor"
    page_size = 20
