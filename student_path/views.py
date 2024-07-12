from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from .models import Path, Student
from .serializers import PathSerializer, StudentSerializer
from .pagination import CustomPageNumberPagination, CustomLimitOffsetPagination


class PathMVS(ModelViewSet):
    queryset = Path.objects.all()
    serializer_class = PathSerializer
    # pagination_class = CustomLimitOffsetPagination


class StudentMVS(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # pagination_class=CustomPageNumberPagination
