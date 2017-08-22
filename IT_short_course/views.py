# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from IT_short_course.models import Round, Player, Match


def home(request):

	# total average score
	yea = []
	test = Round.objects.all()
	for score in test:
		yea.append(score.to_par)
	total_average_score = round((sum(yea)) / float(test.count()), 3)

	# total average hole
	holding = []
	all_rounds = Round.objects.all()
	for avg_hole in all_rounds:
		holding.append(avg_hole.average_hole_score())
	total_average_hole = round((sum(holding)) / float(all_rounds.count()), 3)

	# total aces 
	aces = []
	for ace in all_rounds:
		aces.append(ace.ace_count())
	total_aces = sum(aces)

	# total birdies 
	birdies = []
	for birdie in all_rounds:
		birdies.append(birdie.birdie_count())
	total_birdies = sum(birdies)

	# total pars 
	pars = []
	for par in all_rounds:
		pars.append(par.par_count())
	total_pars = sum(pars)

	# total bogies 
	bogies = []
	for bogie in all_rounds:
		bogies.append(bogie.bogie_count())
	total_bogies = sum(bogies)

	# total doubles 
	doubles = []
	for double in all_rounds:
		doubles.append(double.double_count())
	total_doubles = sum(doubles)

	# total trips and over 
	trips = []
	for trip in all_rounds:
		trips.append(trip.trip_and_over_count())
	total_trips_and_above = sum(trips)



	context = {
		'all_rounds': all_rounds,
		'all_players': Player.objects.all(),
		'all_matches': Match.objects.all(),
		'total_average_score': total_average_score,
		'total_average_hole': total_average_hole,
		'total_aces': total_aces,
		'total_birdies': total_birdies,
		'total_pars': total_pars,
		'total_bogies': total_bogies,
		'total_doubles': total_doubles,
		'total_trips_and_above': total_trips_and_above
	}
	return render(request, 'home.html', context)


