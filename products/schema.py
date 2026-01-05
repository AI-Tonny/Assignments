from django.contrib.auth.models import User
from graphene import ObjectType, Mutation, List, Field, ID, String, Decimal, Boolean
from graphene_django import DjangoObjectType

from .models import Product

class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ["id", "username", "email"]

class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        fields = ["id", "name", "description", "price", "is_available", "user"]

class CreateProductMutation(Mutation):
    class Arguments:
        name = String(required=True)
        price = Decimal(required=True)
        description = String()

    product = Field(ProductType)

    def mutate(self, info, name, price, description=None):
        user = info.context.user

        if user.is_anonymous:
            raise Exception("Authentication required")

        new_product = Product(
            name=name,
            price=price,
            description=description,
            user=user
        )

        new_product.save()
        return CreateProductMutation(product=new_product)

class UpdateProductMutation(Mutation):
    class Arguments:
        id = ID(required=True)
        name = String()
        description = String()
        price = Decimal()
        is_available = Boolean()

    product = Field(ProductType)
    ok = Boolean()

    def mutate(self, info, id, name=None, description=None, price=None, is_available=None):
        try:
            product_instance = Product.objects.get(pk=id)

            if product_instance.user != info.context.user:
                raise Exception("This product doesn't belong to you, and you can't change it.")
        except Product.DoesNotExist:
            return UpdateProductMutation(ok=False, product=None)

        if name is not None:
            product_instance.name = name
        if description is not None:
            product_instance.description = description
        if price is not None:
            product_instance.price = price
        if is_available is not None:
            product_instance.is_available = is_available

        product_instance.save()
        return UpdateProductMutation(ok=True, product=product_instance)

class DeleteProductMutation(Mutation):
    class Arguments:
        id = ID(required=True)

    ok = Boolean()

    def mutate(self, info, id):
        try:
            news_instance = Product.objects.get(pk=id)
            news_instance.delete()
            return DeleteProductMutation(ok=True)
        except Product.DoesNotExist:
            return DeleteProductMutation(ok=False)

class Mutation(ObjectType):
    create_product = CreateProductMutation.Field()
    update_product = UpdateProductMutation.Field()
    delete_product = DeleteProductMutation.Field()

class Query(ObjectType):
    all_products = List(ProductType, search=String())

    def resolve_all_products(self, info, search=None):
        if search:
            return Product.objects.filter(name__icontains=search).select_related('user').all()
        return Product.objects.select_related('user').all()