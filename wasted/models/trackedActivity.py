from django.db import models
from wasted.models.activity import Activity
import datetime
from wasted.models.user import Person


class TrackedActivity(models.Model):
    activity = models.ForeignKey(Activity)
    startTime = models.DateTimeField(default=datetime.datetime.utcnow())
    endTime = models.DateTimeField(null=True)
    position = models.CharField(max_length=128)
    user = models.ForeignKey(Person)

    @classmethod
    def create(cls, activity_id, user_id, position):
        person = Person.objects.get(id=user_id)
        activity = Activity.objects.get(id=activity_id)
        trackedActivity = cls(activity=activity,
                              user=person,
                              position=position)
        trackedActivity.save()
        return trackedActivity
