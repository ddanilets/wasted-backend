from wasted.models.friendList import FriendList
from wasted.models.user import Person, User
from rest_framework import viewsets
from wasted.serializers.friendList import FriendListSerializer
from rest_framework.response import Response
from rest_framework.decorators import list_route


class FriendListViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = FriendList.objects.all()
    serializer_class = FriendListSerializer
    lookup_field = 'category_id'


    def create(self, request, **kwargs):
        friendName = request.data['friendName']
        user = User.objects.get(username=friendName)
        friend = Person.objects.get(user=user)
        rawFriendListData = {
            'friend_id': friend.id,
            'user_id': request.data['userId'],
        }
        serializer = FriendListSerializer().create(data=rawFriendListData)
        return Response()

    @list_route(methods=['post'])
    def get(self, request):
        userId = request.data['userId']
        friendLists = FriendList.objects.all()
        data = []
        for key in friendLists:
            if key.user_id == userId:
                friend = Person.objects.get(id=key.friend_id)
                friendObj = {
                    'firstName': friend.first_name,
                    'id': friend.id,
                    'lastName': friend.last_name,
                    'username': friend.user.username
                }
                data.append(friendObj)
        return Response(data)