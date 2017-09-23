from rest_framework import serializers
from wasted.serializers.category import CategorySerializer
from wasted.serializers.users import PersonSerializer
from wasted.models.goals import Goal


class GoalsSerializer(serializers.Serializer):
    category = CategorySerializer(required=True)
    name = serializers.CharField(max_length=128)
    type = serializers.CharField(max_length=20)
    user = PersonSerializer(required=True)
    deadline = serializers.DateTimeField()
    timePerDay = serializers.IntegerField()
    id = serializers.IntegerField()

    def create(self, data):
        # Create the user instance
        goal = Goal.create(user_id=data['user_id'],
                           category_id=data['category_id'],
                           goal_type=data['type'],
                           name=data['name'],
                           deadline=data['deadline'],
                           time_per_day=data['time_per_day'])
        return goal
