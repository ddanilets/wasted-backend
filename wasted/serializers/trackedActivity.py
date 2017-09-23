from rest_framework import serializers
from wasted.serializers.activity import ActivitySerializer
from wasted.serializers.users import PersonSerializer
from wasted.models.trackedActivity import TrackedActivity


class TrackedActivitySerializer(serializers.Serializer):
    activity = ActivitySerializer(required=True)
    startTime = serializers.DateTimeField()
    endTime = serializers.DateTimeField()
    position = serializers.CharField(max_length=128)
    user = PersonSerializer(required=True)
    id = serializers.IntegerField()

    def create(self, data):
        # Create the user instance
        trackedActivity = TrackedActivity.create(user_id=data['user_id'],
                                                 activity_id=data['activity_id'],
                                                 position=data['position'])
        return trackedActivity
