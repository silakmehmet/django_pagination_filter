from django.db import models


class Path(models.Model):
    path_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.path_name}"


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    number = models.IntegerField()
    path = models.ForeignKey(Path, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
