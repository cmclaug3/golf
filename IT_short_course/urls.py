from django.conf.urls import url, include
from django.contrib import admin

from IT_short_course.views import home, single_player

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^player/(?P<player_id>[0-9]+)$', single_player, name='single_player'),
]