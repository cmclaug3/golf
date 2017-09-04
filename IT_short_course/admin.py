# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from IT_short_course.models import Player, Match, Round, Course


admin.site.register(Player)
admin.site.register(Match)
admin.site.register(Round)
admin.site.register(Course)