from graphene import ObjectType, Schema

import news.schema
import products.schema

class Query(news.schema.Query, products.schema.Query, ObjectType):
    pass

class Mutation(news.schema.Mutation, products.schema.Mutation, ObjectType):
    pass

schema = Schema(query=Query, mutation=Mutation)
