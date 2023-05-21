from django.shortcuts import render
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination
from .pagination import MyPagination, MyPagination2, MyPagination3


class EmployeeListView(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    pagination_class = MyPagination3

