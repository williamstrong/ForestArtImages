from graphene import relay
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from .models import Category, Image

class ImageNode(DjangoObjectType):
    class Meta:
        model = Image
        filter_fields = ['id', 'name', 'category__name']
        interfaces = (relay.Node, )

    @classmethod
    def get_node(cls, info, id):
        return Image.objects.get(id=id)

class CategoryNode(DjangoObjectType):
    class Meta:
        model = Category
        filter_fields = []
        interfaces = (relay.Node, )

    def get_node(cls, info, id):
        return Category.object.get(id=id)

class Query(object):
    image = relay.Node.Field(ImageNode)
    images = DjangoFilterConnectionField(ImageNode)

    category = relay.Node.Field(CategoryNode)
    categories = DjangoFilterConnectionField(CategoryNode)
