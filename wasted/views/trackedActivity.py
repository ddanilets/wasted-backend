from wasted.models.trackedActivity import TrackedActivity
from wasted.models.user import Person
import datetime
from rest_framework import viewsets
from wasted.serializers.trackedActivity import TrackedActivitySerializer
from rest_framework.response import Response
from rest_framework.decorators import list_route


class TrackedActivityViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = TrackedActivity.objects.all()
    serializer_class = TrackedActivitySerializer
    lookup_field = 'category_id'


    def create(self, request, **kwargs):
        rawTrackedActivityData = {
            'activity_id': request.data['activityId'],
            'user_id': request.data['userId'],
            'position': request.data['position'],
        }
        serializer = TrackedActivitySerializer().create(data=rawTrackedActivityData)
        return Response()

    @list_route(methods=['post'])
    def finish(self, request):
        activityId = request.data['id']
        activityLists = TrackedActivity.objects.all()
        for key in activityLists:
            if activityId == key.id:
                key.endTime = datetime.datetime.utcnow()
                key.save()
        return Response()

    @list_route(methods=['post'])
    def get(self, request):
        userId = request.data['userId']
        activityLists = TrackedActivity.objects.all()
        data = []
        for key in activityLists:
            if key.user.id == userId:
                activityObj = {
                    'name': key.name,
                    'activity': {
                        'id': key.activity.id,
                        'name': key.activity.name,
                        'category': {
                            'id': key.activity.category.id,
                            'name': key.activity.category.name,
                        }
                    },
                    'startTime': key.startTime,
                    'position': key.position,
                }
                data.append(activityObj)
        return Response(data)