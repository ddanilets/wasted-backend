from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)

    @classmethod
    def create(cls, name):
        category = cls(name=name)
        category.save()
        return category
