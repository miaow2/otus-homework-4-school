import graphene

from courses.schema import Mutation as CourseMutation, Query as CourseQuery


class Query(CourseQuery, graphene.ObjectType):
    pass


class Mutation(CourseMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
