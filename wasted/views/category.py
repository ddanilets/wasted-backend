from wasted.models.category import Category
from rest_framework import viewsets
from wasted.serializers.category import CategorySerializer
from rest_framework.response import Response


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'category_id'


    def create(self, request, **kwargs):
        rawCategoryData = {
            'name': request.data['name'],
        }
        serializer = CategorySerializer().create(data=rawCategoryData)
        return Response()
