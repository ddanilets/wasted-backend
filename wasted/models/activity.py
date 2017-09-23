from django.db import models
from wasted.models.category import Category


class Activity(models.Model):
    name = models.CharField(max_length=128, unique=True)
    category = models.ForeignKey(Category)

    @classmethod
    def create(cls, name, category_id):
        category = Category.objects.get(id=category_id)
        activity = cls(name=name, category=category)
        activity.save()
        return activity
