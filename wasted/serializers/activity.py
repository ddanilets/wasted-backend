from wasted.models.activity import Activity
from wasted.serializers.category import CategorySerializer
from rest_framework import serializers


class ActivitySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=128)
    category = CategorySerializer(required=True)

    def create(self, data):
        # Create the user instance
        activity = Activity.create(name=data['name'], category_id=data['category_id'])
        return activity
