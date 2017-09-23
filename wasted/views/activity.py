from wasted.models import activity
from rest_framework import viewsets
from wasted.serializers.activity import ActivitySerializer
from django.core.exceptions import SuspiciousOperation
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import list_route, detail_route
from wasted.utils.utils import get_user_id_by_session_id


class ActivityViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = activity.Activity.objects.all()
    serializer_class = ActivitySerializer
    lookup_field = 'activity_id'


    def create(self, request, **kwargs):
        rawActivityData = {
            'name': request.data['name'],
            'category_id': request.data['categoryId'],
        }
        serializer = ActivitySerializer().create(data=rawActivityData)
        return Response()
