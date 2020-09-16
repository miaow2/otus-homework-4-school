import factory
from django.core.management import BaseCommand
from typing import Any, Optional

from courses.models import CATEGORIES, Course


class CourseFactory(factory.django.DjangoModelFactory):

    name = factory.Faker('word')
    category = factory.Faker('random_element', elements=[x[0] for x in CATEGORIES])
    duration = factory.Faker('random_digit_not_null')
    description = factory.Faker('word')

    class Meta:
        model = Course


def create_all():
    course = CourseFactory.build_batch(5)
    print(course)


class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        self.stdout.write("Run Factory Boy")
        create_all()
