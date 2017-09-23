from django.db import models
from wasted.models import user


class FriendList(models.Model):
    friend = models.ForeignKey(user.Person)
    user = models.ForeignKey(user.Person)

    @classmethod
    def create(cls, user_id, friend_id):
        userEntity = user.Person.objects.get(id=user_id)
        friend = user.Person.objects.get(id=friend_id)
        friendList = cls(user=userEntity, friend=friend)
        friendList.save()
        return friendList
