from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination

class MyPagination(PageNumberPagination):
    page_size = 10
    page_query_param = 'mypage'  # default value is 'page'
    page_size_query_param = 'num'  # default value is 'page size', no of records per page
    max_page_size = 15  # max no of records per page
    last_page_strings = ('endpage',)  # default value is 'last'
class MyPagination2(LimitOffsetPagination):
    default_limit = 15
    limit_query_param = 'perpage'
    offset_query_param = 'startat'
    max_limit = 20
class MyPagination3(CursorPagination):
    ordering = 'esal'
    page_size = 5
