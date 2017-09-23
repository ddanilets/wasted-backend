from wasted.models.goals import Goal
from wasted.models.user import Person
from rest_framework import viewsets
from wasted.serializers.goals import GoalsSerializer
from rest_framework.response import Response
from rest_framework.decorators import list_route


class GoalsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Goal.objects.all()
    serializer_class = GoalsSerializer
    lookup_field = 'category_id'


    def create(self, request, **kwargs):
        rawGoalData = {
            'name': request.data['name'],
            'user_id': request.data['userId'],
            'category_id': request.data['categoryId'],
            'type': request.data['type'],
            'deadline': request.data['deadline'],
            'time_per_day': request.data['timePerDay'],
        }
        serializer = GoalsSerializer().create(data=rawGoalData)
        return Response()

    @list_route(methods=['post'])
    def get(self, request):
        userId = request.data['userId']
        goalLists = Goal.objects.all()
        data = []
        for key in goalLists:
            if key.user_id == userId:
                goalObj = {
                    'name': key.name,
                    'category': {
                        'id': key.category.id,
                        'name': key.category.name
                    },
                    'type': key.type,
                    'deadline': key.deadline,
                    'timePerDay': key.timePerDay
                }
                data.append(goalObj)
        return Response(data)