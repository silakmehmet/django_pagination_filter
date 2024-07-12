from rest_framework import serializers

from .models import Path, Student


class PathSerializer(serializers.ModelSerializer):
    class Meta:
        model = Path
        fields = "__all__"
        read_only_fields = ("id")


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
        read_only_fields = ("id")
