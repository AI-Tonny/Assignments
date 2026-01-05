from django.contrib.auth.models import User
from graphene import ObjectType, Mutation, List, Field, ID, String, Boolean
from graphene_django import DjangoObjectType

from .models import News

class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ["id", "username", "email"]

class NewsType(DjangoObjectType):
    class Meta:
        model = News
        fields = ["id", "title", "content", "image_url", "created_at", "author"]

class CreateNewsMutation(Mutation):
    class Arguments:
        title = String(required=True)
        content = String()
        image_url = String()

    news = Field(NewsType)

    def mutate(self, info, title, content=None, image_url=None):
        user = info.context.user

        if user.is_anonymous:
            raise Exception("Authentication required")

        new_news = News(
            title=title,
            content=content,
            image_url=image_url,
            author=user
        )

        new_news.save()
        return CreateNewsMutation(news=new_news)

class UpdateNewsMutation(Mutation):
    class Arguments:
        id = ID(required=True)
        title = String()
        content = String()
        image_url = String()

    news = Field(NewsType)
    ok = Boolean()

    def mutate(self, info, id, title=None, content=None, image_url=None):
        try:
            news_instance = News.objects.get(pk=id)
        except News.DoesNotExist:
            return UpdateNewsMutation(ok=False, news=None)

        if title is not None:
            news_instance.title = title
        if content is not None:
            news_instance.content = content
        if image_url is not None:
            news_instance.image_url = image_url

        news_instance.save()
        return UpdateNewsMutation(ok=True, news=news_instance)

class DeleteNewsMutation(Mutation):
    class Arguments:
        id = ID(required=True)

    ok = Boolean()

    def mutate(self, info, id):
        try:
            news_instance = News.objects.get(pk=id)
            news_instance.delete()
            return DeleteNewsMutation(ok=True)
        except News.DoesNotExist:
            return DeleteNewsMutation(ok=False)

class Mutation(ObjectType):
    create_news = CreateNewsMutation.Field()
    update_news = UpdateNewsMutation.Field()
    delete_news = DeleteNewsMutation.Field()

class Query(ObjectType):
    all_news = List(NewsType)

    def resolve_all_news(self, info):
        return News.objects.select_related('author').all()