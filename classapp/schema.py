import graphene
from graphene_django import DjangoObjectType, DjangoListField, DjangoConnectionField
from .models import Category, Post


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = '__all__'


class PostType(DjangoObjectType):
    class Meta:
        model = Post
        fields = '__all__'


class Query(graphene.ObjectType):
    all_categoroy = DjangoListField(CategoryType)
    all_post = DjangoListField(PostType)


class CategoryMutation(graphene.Mutation):
    pass


schema = graphene.Schema(query=Query)
