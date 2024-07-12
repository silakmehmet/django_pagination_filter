from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet

from .models import Path, Student
from .serializers import PathSerializer, StudentSerializer
from .pagination import CustomPageNumberPagination, CustomLimitOffsetPagination, CustomCursorPagination


class PathMVS(ModelViewSet):
    queryset = Path.objects.all()
    serializer_class = PathSerializer
    # pagination_class = CustomLimitOffsetPagination
    # filterset_fields = ["path_name"]


class StudentMVS(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = CustomPageNumberPagination
    # pagination_class = CustomCursorPagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ["first_name", "number"]
    search_fields = ["first_name", "last_name"]
