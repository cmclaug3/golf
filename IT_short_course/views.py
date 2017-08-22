# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from IT_short_course.models import Round, Player, Match


def home(request):

	yea = []
	test = Round.objects.all()
	for score in test:
		yea.append(score.to_par)
	total_average_score = (sum(yea)) / test.count

	context = {
		'all_rounds': Round.objects.all(),
		'all_players': Player.objects.all(),
		'all_matches': Match.objects.all(),
		'total_average_score': total_average_score
	}
	return render(request, 'home.html', context)


