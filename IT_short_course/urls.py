from django.conf.urls import url, include
from django.contrib import admin

from IT_short_course.views import home, single_player, matches, match, all_player_stats

urlpatterns = [
    
    url(r'^player/(?P<player_id>[0-9]+)$', single_player, name='single_player'),
    url(r'^match/(?P<match_id>[0-9]+)$', match, name='match'),
    url(r'^matches$', matches, name='matches'),
    url(r'^all_player_stats$', all_player_stats, name='all_player_stats'),
    url(r'^$', home, name='home'),
]