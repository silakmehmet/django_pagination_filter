from .models import Path, Student

from faker import Faker


def run():
    fake = Faker(["tr-TR"])

    paths = (
        "FullStack Developer",
        "Data Science",
        "AWS Devops",
        "Backend Developer"
    )

    for path in paths:
        new_path = Path.objects.create(path_name=path)

        for _ in range(50):
            Student.objects.create(first_name=fake.first_name(
            ), last_name=fake.last_name(), number=fake.pyint(), path=new_path)

    print("Bitti")
