"""ignat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from rest_framework import routers
from wasted.views import activity, category, users, friendList, goals, trackedActivity
from django.contrib import admin

router = routers.DefaultRouter()
router.register(r'users', users.UserViewSet)
router.register(r'activities', activity.ActivityViewSet)
router.register(r'categories', category.CategoryViewSet)
router.register(r'friends', friendList.FriendListViewSet)
router.register(r'goals', goals.GoalsViewSet)
router.register(r'trackedActivity', trackedActivity.TrackedActivityViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
