import graphene
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from users.models import User
from .models import Course, Lesson


class CourseType(DjangoObjectType):

    class Meta:
        model = Course


class LessonType(DjangoObjectType):

    class Meta:
        model = Lesson


class UserType(DjangoObjectType):

    class Meta:
        model = User


class CourseFilteredType(DjangoObjectType):

    class Meta:
        model = Course
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
        }
        interfaces = (graphene.relay.Node, )


class ProfessorFilteredType(DjangoObjectType):

    class Meta:
        model = User
        filter_fields = {
            'professor': ['exact'],
        }
        interfaces = (graphene.relay.Node, )


class StudentFilteredType(DjangoObjectType):

    class Meta:
        model = User
        filter_fields = {
            'student': ['exact'],
        }
        interfaces = (graphene.relay.Node, )


class CourseMutation(graphene.Mutation):

    class Arguments:
        course_id = graphene.Int(required=True)
        new_name = graphene.String(required=True)

    result = graphene.Boolean()
    course = graphene.Field(CourseType)

    def mutate(self, info, course_id, new_name):
        course = Course.objects.get(id=course_id)
        course.name = new_name
        course.save()
        return {
            'result': True,
            'course': Course.objects.get(id=course_id)
        }


class StudentMutation(graphene.Mutation):

    class Arguments:
        username = graphene.String(required=True)
        new_name = graphene.String(required=True)

    result = graphene.Boolean()
    student = graphene.Field(UserType)

    def mutate(self, info, username, new_name):
        student = User.objects.get(username=username)
        student.first_name = new_name
        student.save()
        return {
            'result': True,
            'student': User.objects.get(username=username)
        }


class Mutation:
    change_course_name = CourseMutation.Field()
    change_student_first_name = StudentMutation.Field()


class Query:
    all_courses = graphene.List(CourseType, limit=graphene.Int())
    get_course_id = graphene.Field(CourseType, id=graphene.Int())
    get_course_name = graphene.Field(CourseType, name=graphene.String())
    filtered_courses = DjangoFilterConnectionField(CourseFilteredType)
    filtered_students = DjangoFilterConnectionField(StudentFilteredType)
    filtered_professors = DjangoFilterConnectionField(ProfessorFilteredType)

    def resolve_all_courses(self, *args, **kwargs):
        if 'limit' in kwargs:
            return Course.objects.all()[:kwargs['limit']]
        return Course.objects.all()

    def resolve_get_course_id(self, *args, **kwargs):
        if 'id' in kwargs:
            return Course.objects.get(id=kwargs['id'])

    def resolve_get_course_name(self, *args, **kwargs):
        if 'name' in kwargs:
            return Course.objects.get(name=kwargs['name'])
