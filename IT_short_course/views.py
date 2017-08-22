# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from IT_short_course.models import Round, Player, Match


def home(request):
	context = {
		'all_rounds': Round.objects.all(),
		'all_players': Player.objects.all(),
		'all_matches': Match.objects.all(), 
	}
	return render(request, 'home.html', context)


