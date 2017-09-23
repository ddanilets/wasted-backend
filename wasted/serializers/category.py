from wasted.models import category
from rest_framework import serializers


class CategorySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=128)
    id = serializers.IntegerField()

    def create(self, data):
        # Create the user instance
        person = category.Category.create(name=data['name'])
        return person
