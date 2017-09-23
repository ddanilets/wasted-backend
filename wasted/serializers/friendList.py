from wasted.models.friendList import FriendList
from wasted.serializers.users import PersonSerializer
from rest_framework import serializers


class FriendListSerializer(serializers.Serializer):
    friend = PersonSerializer(required=True)
    user = PersonSerializer(required=True)

    def create(self, data):
        # Create the user instance
        friendList = FriendList.create(user_id=data['user_id'], friend_id=data['friend_id'])
        return friendList
