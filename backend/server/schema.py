import graphene
from graphene_django.types import DjangoObjectType
from .models import Macronutrients, User, TestModel  # replace YourModel with your actual model

class MacronutrientsType(DjangoObjectType):
    class Meta:
        model = Macronutrients
        fields = ("id", "calories", "carbohydrates", "fats", "proteins", "fiber", "water")
    id = graphene.ID(source='pk')

class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ("id", "name", "email", "password", "age", "weight", "height", "macros")

class Query(graphene.ObjectType):
    all_items = graphene.List(MacronutrientsType)
    find_user = graphene.Field(UserType, id=graphene.ID())

    def resolve_all_items(self, info):
        return Macronutrients.objects.all()
    
    def resolve_find_user(self, info, id):
        return User.objects.get(pk=id)

schema = graphene.Schema(query=Query)