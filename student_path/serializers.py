from rest_framework import serializers

from .models import Path, Student


class PathSerializer(serializers.ModelSerializer):
    students = serializers.SerializerMethodField()

    class Meta:
        model = Path
        fields = "__all__"
        read_only_fields = ("id",)

    def get_students(self, obj):
        students = obj.student_set.all()
        serializer = StudentSerializer(students, many=True)
        return serializer.data


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
        read_only_fields = ("id",)
