from django.db import models
from wasted.models.category import Category
from wasted.models.user import Person


class Goal(models.Model):
    name = models.CharField(max_length=128, unique=True)
    user = models.ForeignKey(Person)
    category = models.ForeignKey(Category)
    type = models.CharField(max_length=20)
    deadline = models.DateTimeField()
    timePerDay = models.IntegerField()

    @classmethod
    def create(cls, category_id, user_id, goal_type, name, deadline, time_per_day):
        category = Category.objects.get(id=category_id)
        person = Person.objects.get(id=user_id)
        goal = cls(name=name, category=category, user=person, type=goal_type, deadline=deadline, timePerDay=time_per_day)
        goal.save()
        return goal
